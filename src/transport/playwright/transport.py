# STANDARD IMPORTS
import time

# THIRD PART IMPORTS
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    results = page.locator('title:has-text("Lenovo")')

    count = results.count()

    for i in range(count):
        element = results.nth(i)
        text = element.inner_text()

        print(text)
