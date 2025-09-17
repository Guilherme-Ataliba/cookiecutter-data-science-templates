{% if cookiecutter.project_type == "crawler" and cookiecutter.crawler_type == "httpx" %}
import httpx
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
{% elif cookiecutter.project_type == "crawler" and cookiecutter.crawler_type == "aiohttp" %}
import asyncio
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
{% elif cookiecutter.project_type == "none" %}
# Basic Python project - no specific template
print("Hello, World!")
{% endif %}
