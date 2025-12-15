from fastapi import (
    APIRouter,
    HTTPException,
    Request,
    status,
)

from app.models import (
    Item,
    ItemUpdate,
)

router = APIRouter()


@router.get("/health")
def get_health():
    return {"status": "ok"}


@router.get("/items")
def get_items(request: Request):
    items = list(request.app.database["items"].find({}, {"_id": 0}))
    return {"items": items}


@router.post("/items", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_item(item: Item, request: Request):
    # Get the next available item_id
    last_item = request.app.database["items"].find_one(
        {"item_id": {"$exists": True}}, sort=[("item_id", -1)]
    )
    next_id = 1 if not last_item else last_item.get("item_id", 0) + 1

    item_dict = item.model_dump()
    item_dict["item_id"] = next_id
    request.app.database["items"].insert_one(item_dict)

    return {
        "message": "Item created successfully",
        "item": {k: v for k, v in item_dict.items() if k != "_id"},
    }


@router.get("/items/{item_id}")
def get_item(item_id: int, request: Request):
    item = request.app.database["items"].find_one({"item_id": item_id}, {"_id": 0})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item": item}


@router.put("/items/{item_id}")
def update_item(item_id: int, item_update: ItemUpdate, request: Request):
    update_data = {k: v for k, v in item_update.model_dump().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = request.app.database["items"].update_one(
        {"item_id": item_id}, {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = request.app.database["items"].find_one(
        {"item_id": item_id}, {"_id": 0}
    )

    return {"message": "Item updated successfully", "item": updated_item}


@router.delete("/items/{item_id}")
def delete_item(item_id: int, request: Request):
    result = request.app.database["items"].delete_one({"item_id": item_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item deleted successfully"}
