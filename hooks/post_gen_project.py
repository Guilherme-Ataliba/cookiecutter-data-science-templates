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

# Template-specific packages and conditional logic
if "{{ cookiecutter.project_type }}" == "crawler":
    # Prompt for crawler type only when project_type is crawler
    import sys
    print("\nSelect crawler type:")
    print("1 - httpx")
    print("2 - aiohttp")
    
    while True:
        try:
            choice = input("Choose from [1, 2] (1): ").strip()
            if not choice:
                choice = "1"
            
            if choice == "1":
                crawler_type = "httpx"
                packages_to_install += ["httpx"]
                break
            elif choice == "2":
                crawler_type = "aiohttp"
                packages_to_install += ["aiohttp"]
                break
            else:
                print("Please choose 1 or 2")
        except KeyboardInterrupt:
            sys.exit(1)
    
    # Create the appropriate main.py file
    main_py_content = ""
    if crawler_type == "httpx":
        main_py_content = '''import httpx
import asyncio


async def main():
    """Main function for httpx-based web scraping."""
    async with httpx.AsyncClient() as client:
        # Example: Make a GET request
        response = await client.get("https://httpbin.org/get")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")


if __name__ == "__main__":
    asyncio.run(main())
'''
    elif crawler_type == "aiohttp":
        main_py_content = '''import asyncio
import aiohttp


async def main():
    """Main function for aiohttp-based web scraping."""
    async with aiohttp.ClientSession() as session:
        # Example: Make a GET request
        async with session.get("https://httpbin.org/get") as response:
            data = await response.json()
            print(f"Status: {response.status}")
            print(f"Response: {data}")


if __name__ == "__main__":
    asyncio.run(main())
'''
    
    # Write the main.py file
    with open("main.py", "w") as f:
        f.write(main_py_content)
else:
    # Remove main.py for non-crawler projects
    if Path("main.py").exists():
        Path("main.py").unlink()

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
# No special post-installation steps needed for current templates