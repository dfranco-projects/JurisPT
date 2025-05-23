import json
from tqdm import tqdm
from os.path import join, dirname, abspath
from playwright.sync_api import Playwright, sync_playwright
from utils import normalize_law_filename, mark_law_as_revoked

class LawScraper:
    def __init__(self) -> None:
        self.crawler_folder = dirname(abspath(__file__))
        self.src_folder = dirname(self.crawler_folder)
        self.root_folder = dirname(self.src_folder)
        self.corpus_folder = join(self.root_folder, "corpus")
        self.raw_folder = join(self.corpus_folder, "raw")
        self.metadata_folder = join(self.corpus_folder, "metadata")
        self.metadata = join(self.metadata_folder, "laws_metadata.json")
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

    def open(self) -> None:
        """
        Opens the website.
        """
        self.page.goto(self.url)
        
    def close(self) -> None:
        """
        Closes the browser and context.
        """
        self.context.close()
        self.browser.close()

    def fetch_law_doc(self, law_id: str) -> tuple[str, bool]:
        """
        Fetches the law document from the website and checks if it is revoked.

        Args:
            law_id (str): ID of the law to fetch.

        Returns:        
            tuple: (content of the law document, is_active)
        """
        page = self.page

        # search
        page.get_by_placeholder("O que procura?").fill(law_id)

        # wait for law search popup and open it
        page.wait_for_selector('//*[@id="b2-b2-b3-AutoCompleteSuggestions"]', timeout=1_000)
        page.locator('//*[@id="b2-b2-b3-AutoCompleteSuggestions"]').click()
        
        # wait for the content to load (5 sec)
        page.wait_for_selector(".texto.int-links", timeout=5_000)

        # get law content
        content = page.locator(".texto.int-links").inner_text()

        # check if revoked
        vigencia_element = page.query_selector('xpath=//*[@id="b7-Vigencia"]')
        if vigencia_element is not None:
            vigencia_text = vigencia_element.inner_text()
            is_active = "revogado" not in vigencia_text.lower()
        else:
            # if the element does not exist, consider the law active
            is_active = True

        return content, is_active
    
    def write_law_doc(self, law_id: str, content: str) -> None:
        """
        Writes law content to a .txt file inside the raw corpus folder.

        Args:
            law_id (str): law ID used to name the file.
            content (str): raw text content to save.
        """
        filename = normalize_law_filename(law_id) + ".txt"
        file_path = join(self.raw_folder, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    def run_test_scraper(self, law_id, laws_metadata=None) -> tuple[str, list]:
        """
        Tests the scraper ability to fetch the law document and update the metadata if revoked.

        Args:
            law_id (str): ID of the law to fetch.
            law_metadata (list): list of law metadata dict. Defaults to None.
            
        Returns:
            tuple: (content of the law document, updated laws_metadata list)
        """
        with sync_playwright() as playwright:
            self.setup(playwright)
            self.open()
            content, is_active = self.fetch_law_doc(law_id)
            if laws_metadata and not is_active: # check if the law is active
                laws_metadata = mark_law_as_revoked(laws_metadata, law_id)
            self.close()
        return content, laws_metadata
    
    def run_scraper(self) -> None:
        """
        Downloads and saves the laws listed in the metadata file to the raw corpus folder.
        """
        # load laws metadata
        with open(self.metadata) as f:
            laws_metadata = json.load(f)

        with sync_playwright() as playwright:
            self.setup(playwright)
            self.open()
            for law in tqdm(laws_metadata, desc="Scraping laws"):
                law_id = law["law_id"]
                active = law["active"]
                if active: # check if the law is active
                    content, is_active = self.fetch_law_doc(law_id)
                    if not is_active: # if not mark as revoked
                        laws_metadata = mark_law_as_revoked(laws_metadata, law_id)
                    else:
                        self.write_law_doc(law_id, content)
            self.close()
        # save the updated metadata
        with open(self.metadata, "w", encoding="utf-8") as f:
            json.dump(laws_metadata, f, ensure_ascii=False, indent=4)
    
if __name__ == "__main__":
    crawler = LawScraper()
    crawler.run_scraper()