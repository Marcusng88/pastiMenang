# PastiMenang 🌞

A powerful solar investigation agent powered by Google AI that analyzes solar energy data and provides insights for renewable energy projects.

## Features

- **AI-Powered Analysis**: Leverages Google's advanced AI models for intelligent solar data processing
- **Multi-Agent Architecture**: Includes specialized sub-agents for different aspects of solar investigation
- **Visualization Support**: Built-in visualization tools for data analysis and reporting
- **ADK Integration**: Built with Google's Agent Development Kit for seamless development and deployment

## Quick Start

### Prerequisites

- Python 3.13 or higher
- UV package manager
- Google ADK (Agent Development Kit)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd pastiMenang
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Install development dependencies:**
   ```bash
   uv sync --group dev
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your Google Cloud credentials and API keys
   ```

### Development with ADK

Start the development server with the Agent Development Kit:

```bash
adk web
```

This will launch the ADK web interface where you can:
- Test your agent interactively
- Debug agent responses
- Monitor performance
- Access built-in development tools

The ADK provides a complete development environment, so you don't need to run the agent directly through Python files.

## Development

### Setting up Development Environment

1. **Install development dependencies:**
   ```bash
   uv sync --group dev
   ```

2. **Install pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

### Code Quality

This project uses several tools to maintain code quality:

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checking
- **Pytest**: Testing framework
- **Pre-commit**: Git hooks for automated checks

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=solar_investigator

# Run specific test file
uv run pytest tests/test_agent.py
```

### Code Formatting and Linting

```bash
# Format code with Ruff
uv run ruff format .

# Lint code with Ruff
uv run ruff check .

# Fix auto-fixable linting issues
uv run ruff check --fix .

# Type checking with MyPy
uv run mypy solar_investigator/
```

### Project Structure

```
pastiMenang/
├── solar_investigator/          # Main package
│   ├── __init__.py
│   ├── agent.py                 # Main agent implementation
│   ├── prompts.py              # AI prompts and templates
│   ├── tools.py                # Agent tools and utilities
│   └── sub_agents/             # Specialized sub-agents
│       └── visualization_agent/ # Data visualization agent
├── tests/                      # Test suite
├── main.py                     # Application entry point
├── pyproject.toml             # Project configuration
├── uv.lock                    # Dependency lock file
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## Configuration

Create a `.env` file in the project root with the following variables:

```env
# Google AI API Key
GOOGLE_AI_API_KEY=your_api_key_here

# Other configuration options
LOG_LEVEL=INFO
DEBUG=False
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite: `uv run pytest`
5. Run code quality checks: `uv run ruff check .`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep line length to 88 characters (handled by Ruff formatter)

## API Reference

### Main Agent

The main `Agent` class provides the core functionality:

```python
from solar_investigator import Agent

agent = Agent()
result = agent.investigate(query="analyze solar panel efficiency")
```

### Sub-Agents

Specialized agents for specific tasks:

- **VisualizationAgent**: Creates charts and visualizations
- More agents can be added as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Create an issue on GitHub for bug reports or feature requests
- Check the documentation for common questions
- Contact the maintainers for support

## Changelog

### v0.1.0 (Current)
- Initial release
- Basic agent functionality
- Visualization sub-agent
- Google AI integration
