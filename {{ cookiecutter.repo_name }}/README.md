# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Getting Started

### Prerequisites

- Python {{ cookiecutter.python_version_number }}
- uv (for package management)

### Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   uv pip install -e .
   ```

## Usage

This is a minimal data science project template. Add your code to the project root directory.

## Development

- **Linting and Formatting**: This project uses ruff for linting and formatting
- **Package Management**: This project uses uv for dependency management

## License

{% if cookiecutter.open_source_license != "No license file" %}
This project is licensed under the {{ cookiecutter.open_source_license }} License.
{% else %}
No license specified.
{% endif %}
