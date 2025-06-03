#!/bin/bash

# Development setup script for PastiMenang Solar Investigator

set -e

echo "🌞 Setting up PastiMenang Solar Investigator development environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed. Please install it first:"
    echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check if adk is installed
if ! command -v adk &> /dev/null; then
    echo "❌ ADK is not installed. Please install Google Agent Development Kit first."
    exit 1
fi

# Sync dependencies
echo "📦 Installing dependencies..."
uv sync

# Install development dependencies
echo "🔧 Installing development dependencies..."
uv sync --group dev

# Set up pre-commit hooks
echo "🪝 Setting up pre-commit hooks..."
uv run pre-commit install

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env-example .env
    echo "⚠️  Please edit .env file with your Google Cloud credentials!"
fi

# Run initial code quality checks
echo "🔍 Running code quality checks..."
uv run ruff check .
uv run ruff format .

echo "✅ Development environment setup complete!"
echo ""
echo "🚀 To start development:"
echo "   adk web"
echo ""
echo "📝 Don't forget to:"
echo "   1. Edit .env with your Google Cloud credentials"
echo "   2. Set up your Google Cloud project and BigQuery dataset"
echo "   3. Configure your MCP Toolbox URL if needed"
