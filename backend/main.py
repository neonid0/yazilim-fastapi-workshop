import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

from app.routes import router

load_dotenv()
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(os.getenv("MONGODB_CONNECTION_URI"))
    app.database = app.mongodb_client[os.getenv("DB_NAME")]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
