# crawler.py
# responsible for pulling legal text from Diário da República

import re
import json
from playwright.sync_api import Playwright, sync_playwright

class LawCrawler:
    def __init__(self) -> None:
        self.url = "https://diariodarepublica.pt"
        self.browser = None
        self.context = None
        self.page = None

    def setup(self, playwright: Playwright) -> None:
        self.browser = playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close(self) -> None:
        self.browser.close()

    def fetch_law_doc(self, law_id: str) -> str:
        page = self.page
        page.goto(self.url)
        page.get_by_placeholder("O que procura?").fill(law_id)
        page.locator("#b2-b2-b3-l3-252_0-ListItem2").click()
        page.wait_for_load_state()
        page.wait_for_selector(".texto.int-links", timeout=5_000)
        content = page.locator(".texto.int-links").inner_text()
        return content

    def run_scraper(self, law_ids: list[str]) -> list[str]:
        with sync_playwright() as playwright:
            self.setup(playwright)
            results = [self.fetch_law_doc(law_id) for law_id in law_ids]
            self.close()
            return results

    def run_test_scraper(self, law_id: str) -> str:
        with sync_playwright() as playwright:
            self.setup(playwright)
            content = self.fetch_law_doc(law_id)
            self.close()
            return content

if __name__ == "__main__":
    pass
