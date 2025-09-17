{% if cookiecutter.template.crawler == "httpx" %}
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
{% elif cookiecutter.template.crawler == "playwright" %}
import asyncio
from playwright.async_api import async_playwright


async def main():
    """Main function for playwright-based web scraping."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Example: Navigate to a page
        await page.goto("https://example.com")
        title = await page.title()
        print(f"Page title: {title}")
        
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
{% endif %}
