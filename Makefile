.PHONY: help install install-dev test lint format type-check clean run pre-commit

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	uv sync

install-dev: ## Install the package with development dependencies
	uv sync --group dev

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=solar_investigator --cov-report=term-missing --cov-report=html

lint: ## Run linting with ruff
	uv run ruff check .

lint-fix: ## Run linting with ruff and fix issues
	uv run ruff check --fix .

format: ## Format code with ruff
	uv run ruff format .

type-check: ## Run type checking with mypy
	uv run mypy solar_investigator/

pre-commit: ## Run pre-commit hooks on all files
	uv run pre-commit run --all-files

clean: ## Clean up cache and temporary files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/

run: ## Run the main application
	uv run python main.py

dev-setup: install-dev ## Set up development environment
	uv run pre-commit install
	@echo "Development environment set up successfully!"

check: lint type-check test ## Run all checks (lint, type-check, test)

build: ## Build the package
	uv build

publish: ## Publish to PyPI (requires authentication)
	uv publish
