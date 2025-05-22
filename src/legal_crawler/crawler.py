from utils import normalize_filename 
from playwright.sync_api import Playwright, sync_playwright

class LawCrawler:
    def __init__(self) -> None:
        self.url = "https://diariodarepublica.pt"
        self.browser = None
        self.context = None
        self.page = None

    def setup(self, playwright: Playwright) -> None:
        """
        Sets up the scraper by launching the browser and creating a new context.

        Args:
            playwright (Playwright): playwright instance.
        """
        self.browser = playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close(self) -> None:
        """
        Closes the browser and context.
        """
        self.browser.close()

    def fetch_law_doc(self, law_id: str) -> str:
        """
        Fetches the law document from the website.

        Args:
            law_id (str): ID of the law to fetch.

        Returns:        
            str: content of the law document.
        """
        page = self.page

        # open the page
        page.goto(self.url)

        # search
        page.get_by_placeholder("O que procura?").fill(law_id)

        # wait for popup and open it
        page.locator("#b2-b2-b3-l3-269_0-ListItem2").click()

        # wait for the content to load (5 sec)
        page.wait_for_selector(".texto.int-links", timeout=5_000)

        # get law content
        content = page.locator(".texto.int-links").inner_text()

        return content
    
    def save_law_doc(self, law_id: str, content: str) -> Path:
        """
        Saves law content to a normalized filename inside the raw folder.

        Args:
            law_id (str): The law ID used to name the file.
            content (str): The raw text content to save.

        Returns:
            Path: The path to the saved file.
        """
        filename = normalize_filename(law_id)
        file_path = self.raw_folder / filename

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def run_test_scraper(self, law_id) -> str:
        """
        Test the test scraper ability to fetch the law document.

        Args:
            law_id (str): ID of the law to fetch.
            
        Returns:
            str: content of the law document.
        """
        with sync_playwright() as playwright:
            self.setup(playwright)
            content = self.fetch_law_doc(law_id)
            self.close()

            return content

    def run_scraper(self, law_ids: list[str]) -> list[dict]:
        """
        Runs the scraper for the law IDs on the metadata file.

        Args:
            law_ids (list[str]): List of law IDs to fetch.

        Returns:
            list[dict]: List of dictionaries containing law ID and content.
        """
        with sync_playwright() as playwright:
            self.setup(playwright)
            results = [self.fetch_law_doc(law_id) for law_id in law_ids]
            self.close()
            return results
    

        
if __name__ == "__main__":
    pass