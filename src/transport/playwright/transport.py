# THIRD PART IMPORTS
from playwright.sync_api import sync_playwright


class GetScrapFromWebsite:

    @classmethod
    def get_laptops_from_website(cls) -> list:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

            locator_results = page.locator("text=Lenovo")

            results_response = locator_results.all_inner_texts()

            return results_response
