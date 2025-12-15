.PHONY: help install install-backend install-frontend dev dev-backend dev-frontend clean test

help:
	@echo "FastAPI + Next.js Workshop Commands"
	@echo "===================================="
	@echo "make install          - Install all dependencies (backend + frontend)"
	@echo "make install-backend  - Install Python dependencies"
	@echo "make install-frontend - Install Node.js dependencies"
	@echo "make dev              - Run both backend and frontend"
	@echo "make dev-backend      - Run FastAPI backend only"
	@echo "make dev-frontend     - Run Next.js frontend only"
	@echo "make clean            - Clean cache and temporary files"
	@echo "make test             - Run tests (if available)"

install: install-backend install-frontend
	@echo "✓ All dependencies installed!"

install-backend:
	@echo "Installing backend dependencies..."
	cd backend && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

install-frontend:
	@echo "Installing frontend dependencies..."
	cd frontend && pnpm install

dev:
	@echo "Starting backend and frontend..."
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:3000"
	@make -j2 dev-backend dev-frontend

dev-backend:
	@echo "Starting FastAPI backend on http://localhost:8000..."
	cd backend && . .venv/bin/activate && python main.py

dev-frontend:
	@echo "Starting Next.js frontend on http://localhost:3000..."
	cd frontend && pnpm dev

clean:
	@echo "Cleaning cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".next" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".venv" -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cleaned!"

test:
	@echo "Running tests..."
	cd backend && . .venv/bin/activate && python -m pytest || echo "No tests configured"
