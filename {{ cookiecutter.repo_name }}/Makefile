.PHONY: help
help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: create_environment
create_environment: ## Set up the python environment
{% if cookiecutter.environment_manager == "uv" %}
	uv venv
	uv pip install -e .
{% elif cookiecutter.environment_manager == "conda" %}
	conda env create -f environment.yml
	conda activate {{ cookiecutter.repo_name }}
{% elif cookiecutter.environment_manager == "pipenv" %}
	pipenv install
	pipenv install -e .
{% elif cookiecutter.environment_manager == "poetry" %}
	poetry install
{% elif cookiecutter.environment_manager == "pixi" %}
	pixi install
{% elif cookiecutter.environment_manager == "virtualenv" %}
	python -m venv venv
	. venv/bin/activate && pip install -e .
{% endif %}

.PHONY: requirements
requirements: ## Install Python Dependencies
{% if cookiecutter.environment_manager == "uv" %}
	uv pip install -r requirements.txt
{% elif cookiecutter.environment_manager == "conda" %}
	conda env update -f environment.yml
{% elif cookiecutter.environment_manager == "pipenv" %}
	pipenv install
{% elif cookiecutter.environment_manager == "poetry" %}
	poetry install
{% elif cookiecutter.environment_manager == "pixi" %}
	pixi install
{% elif cookiecutter.environment_manager == "virtualenv" %}
	. venv/bin/activate && pip install -r requirements.txt
{% endif %}

.PHONY: clean
clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +

.PHONY: lint
lint: ## Run linting
{% if cookiecutter.linting_and_formatting == "ruff" %}
	ruff check .
	ruff format --check .
{% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %}
	flake8 {{ cookiecutter.repo_name }}
	black --check {{ cookiecutter.repo_name }}
	isort --check-only {{ cookiecutter.repo_name }}
{% endif %}

.PHONY: format
format: ## Run formatting
{% if cookiecutter.linting_and_formatting == "ruff" %}
	ruff format .
{% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %}
	black {{ cookiecutter.repo_name }}
	isort {{ cookiecutter.repo_name }}
{% endif %}
