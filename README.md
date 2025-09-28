# FastAPI Boilerplate with uv and Jinja2

A modern FastAPI boilerplate project using uv as the package manager and Jinja2 for templating.

## Features

- 🚀 **FastAPI**: Modern, fast web framework for building APIs
- 📦 **uv**: Ultra-fast Python package manager
- 🎨 **Jinja2**: Powerful templating engine
- 📱 **Responsive Design**: Mobile-friendly CSS
- 📚 **Auto Documentation**: Built-in API docs with Swagger UI
- ⚡ **Hot Reload**: Development server with auto-reload

## Project Structure

```
fastapi-boilerplate/
├── main.py                 # FastAPI application entry point
├── pyproject.toml         # Project configuration and dependencies
├── README.md              # This file
├── templates/             # Jinja2 templates
│   └── index.html         # Homepage template
└── static/                # Static files
    └── css/
        └── style.css      # Stylesheet
```

## Quick Start

### Prerequisites

- Python 3.8+
- uv package manager

### Install uv

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

### Setup and Run

1. **Clone or create the project directory:**
   ```bash
   mkdir fastapi-boilerplate
   cd fastapi-boilerplate
   ```

2. **Create the project structure:**
   ```bash
   mkdir templates static static/css
   ```

3. **Copy all the files from the artifacts above into their respective locations**

4. **Install dependencies:**
   ```bash
   uv sync
   ```

5. **Run the development server:**
   ```bash
   uv run uvicorn main:app --reload
   ```

6. **Visit your application:**
   - Homepage: http://127.0.0.1:8000
   - API Documentation: http://127.0.0.1:8000/docs
   - Alternative API Docs: http://127.0.0.1:8000/redoc
   - Health Check: http://127.0.0.1:8000/health

## Development

### Adding Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name
```

### Running Tests

```bash
# Install test dependencies first
uv sync --extra dev

# Run tests (when you create them)
uv run pytest
```

### Environment Management

uv automatically manages virtual environments. To activate the environment manually:

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Project Details

### Homepage Sections

The homepage (`templates/index.html`) is structured with three main sections as requested:

1. **Header**: Navigation bar with branding and menu links
2. **Main Body**: Hero section with features and content
3. **Footer**: Links and additional information

### API Endpoints

- `GET /`: Homepage (HTML response)
- `GET /health`: Health check endpoint (JSON response)
- `GET /docs`: Interactive API documentation
- `GET /redoc`: Alternative API documentation

### Styling

The CSS uses modern design principles with:
- CSS Grid and Flexbox for responsive layouts
- Gradient backgrounds
- Smooth transitions and hover effects
- Mobile-first responsive design

### Note:
Generated using AI.