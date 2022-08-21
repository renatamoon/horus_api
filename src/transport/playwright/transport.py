# THIRD PART IMPORTS
from playwright.async_api import async_playwright


class GetScrapFromWebsite:

    @classmethod
    async def get_laptops_from_website(cls) -> list:

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

            locator_results = page.locator("text=Lenovo")

            results_response = await locator_results.all_inner_texts()

            return results_response
