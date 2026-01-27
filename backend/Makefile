.PHONY: help build up down restart logs shell migrate-create migrate-up migrate-down db-shell clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build Docker containers
	docker-compose build

up: ## Start all services
	docker-compose up -d

down: ## Stop all services
	docker-compose down

restart: ## Restart all services
	docker-compose restart

logs: ## View logs
	docker-compose logs -f

logs-backend: ## View backend logs
	docker-compose logs -f backend

logs-postgres: ## View postgres logs
	docker-compose logs -f postgres

shell: ## Access backend shell
	docker-compose exec backend /bin/bash

db-shell: ## Access PostgreSQL shell
	docker-compose exec postgres psql -U postgres -d podcast_db

migrate-create: ## Create a new migration (use MSG="message")
	docker-compose exec backend alembic revision --autogenerate -m "$(MSG)"

migrate-up: ## Run migrations
	docker-compose exec backend alembic upgrade head

migrate-down: ## Rollback last migration
	docker-compose exec backend alembic downgrade -1

migrate-history: ## Show migration history
	docker-compose exec backend alembic history

clean: ## Remove all containers, volumes, and images
	docker-compose down -v
	docker system prune -f

dev: ## Start development environment
	docker-compose up

install: ## Install dependencies locally
	pip install -r requirements.txt

test: ## Run tests
	docker-compose exec backend pytest

format: ## Format code
	docker-compose exec backend black app/
	docker-compose exec backend isort app/
