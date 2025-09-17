from copy import copy
from pathlib import Path

# https://github.com/cookiecutter/cookiecutter/issues/824
#   our workaround is to include these utility functions in the CCDS package
from ccds.hook_utils.dependencies import (
    flake8_black_isort,
    packages,
    ruff,
    write_dependencies,
    write_python_version,
)

#
#  TEMPLATIZED VARIABLES FILLED IN BY COOKIECUTTER
#
# Default packages 
packages_to_install = copy(packages)

# Custom Packages
packages_to_install += [
    "seaborn",
    "sympy",
    "pytest-cov"
]

# Template-specific packages
{% if cookiecutter.template.crawler == "httpx" %}
packages_to_install += ["httpx"]
{% elif cookiecutter.template.crawler == "playwright" %}
packages_to_install += ["playwright"]
{% endif %}

# {% if cookiecutter.linting_and_formatting == "ruff" %}
packages_to_install += ruff
# Remove setup.cfg if it exists
if Path("setup.cfg").exists():
    Path("setup.cfg").unlink()
# {% elif cookiecutter.linting_and_formatting == "flake8+black+isort" %}
packages_to_install += flake8_black_isort
# {% endif %}

# track packages that are not available through conda
pip_only_packages = [
    "python-dotenv",
]

#
#  POST-GENERATION FUNCTIONS
#
write_dependencies(
    "{{ cookiecutter.dependency_file }}",
    packages_to_install,
    pip_only_packages,
    repo_name="{{ cookiecutter.repo_name }}",
    module_name="{{ cookiecutter.repo_name }}",
    python_version="{{ cookiecutter.python_version_number }}",
    environment_manager="{{ cookiecutter.environment_manager }}",
    description="",
)

write_python_version("{{ cookiecutter.python_version_number }}")

# No license handling needed

# Make single quotes prettier
# Jinja tojson escapes single-quotes with \u0027 since it's meant for HTML/JS
pyproject_text = Path("pyproject.toml").read_text()
Path("pyproject.toml").write_text(pyproject_text.replace(r"\u0027", "'"))

# Post-installation steps for specific templates
{% if cookiecutter.template.crawler == "playwright" %}
# Install playwright browser binaries
import subprocess
import sys
subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
{% endif %}