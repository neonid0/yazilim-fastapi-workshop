# FastAPI + Next.js Workshop

A full-stack web application workshop featuring FastAPI backend with MongoDB and Next.js frontend with TypeScript and Tailwind CSS.

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **MongoDB** - NoSQL database with PyMongo
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

### Frontend
- **Next.js 16** - React framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS 4** - Utility-first CSS framework
- **React 19** - Latest React version

## 📋 Prerequisites

- Python 3.8+
- Node.js 18+
- pnpm (or npm/yarn)
- MongoDB (local or Atlas)

## 🛠️ Installation

### Quick Start (All at Once)
```bash
make install
```

### Manual Installation

#### Backend
```bash
make install-backend
# OR
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Frontend
```bash
make install-frontend
# OR
cd frontend
pnpm install
```

## ⚙️ Configuration

Create a `.env` file in the `backend` directory:
- You can copy from `.env.example` and fill in your MongoDB connection details.

```env
MONGODB_CONNECTION_URI=your_mongodb_connection_string
DB_NAME=your_database_name
```

## 🏃 Running the Application

### Run Both Backend and Frontend
```bash
make dev
```
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs

### Run Individually

#### Backend Only
```bash
make dev-backend
# OR
cd backend
source .venv/bin/activate
python main.py
```

#### Frontend Only
```bash
make dev-frontend
# OR
cd frontend
pnpm dev
```

## 🧪 Testing

```bash
make test
```

## 🧹 Cleaning

Remove all cache files, dependencies, and virtual environments:

```bash
make clean
```

## 📁 Project Structure

```
fastapi-workshop/
├── backend/
│   ├── app/
│   │   ├── models.py      # Pydantic models
│   │   └── routes.py      # API endpoints
│   ├── main.py            # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   └── .env              # Environment variables
├── frontend/
│   ├── app/              # Next.js app directory
│   ├── public/           # Static assets
│   ├── package.json      # Node dependencies
│   └── tsconfig.json     # TypeScript config
└── Makefile              # Build automation
```

## 🔧 Available Make Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install all dependencies |
| `make install-backend` | Install Python dependencies |
| `make install-frontend` | Install Node.js dependencies |
| `make dev` | Run both backend and frontend |
| `make dev-backend` | Run FastAPI backend only |
| `make dev-frontend` | Run Next.js frontend only |
| `make clean` | Clean cache and temporary files |
| `make test` | Run tests |

## 🌐 API Endpoints

- `GET /` - Welcome message
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

Additional endpoints defined in `backend/app/routes.py`

## 🤝 Contributing

This is a workshop project. Feel free to experiment and add features!

## 📝 License

This project is open source and available for educational purposes.
