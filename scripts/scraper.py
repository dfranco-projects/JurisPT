from playwright.sync_api import Playwright, sync_playwright, expect

class LawScraper:
    def __init__(self) -> None:
        self.url = "https://diariodarepublica.pt"

    def fetch_law_doc(self, playwright: Playwright, law_id) -> str:
            """
            Fetches the law document from the website.

            Args:
                playwright (Playwright): playwright instance.
                law_id (str): ID of the law to fetch.

            Returns:        
                str: content of the law document.
            """
            browser = playwright.firefox.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(self.url)

            # search
            page.get_by_placeholder("O que procura?").fill(law_id)
            page.get_by_role("button", name="Icon magnifying").click()

            # wait for popup and open it
            # page.locator("#b2-Pesquisa").get_by_text(f"{law_id}", exact=True).click()
            # page.locator("#b2-b2-b3-l3-240_0-ListItem2").click()

            # result_locator = page.locator("#b2-b2-b3-l3-240_0-ListItem2")
            # result_locator.wait_for(state="visible", timeout=5000)
            # result_locator.hover()

            # print("Before click URL:", page.url)
            # result_locator.click()
            # page.wait_for_load_state("networkidle")
            # print("After click URL:", page.url)


            #######################
            
            with page.expect_popup() as popup_info:
                page.get_by_role("link", name=f"{law_id} -").click()
            law_page = popup_info.value
            law_page.wait_for_load_state()

            ########################


            # wait for the content to load (5 sec)
            law_page.wait_for_load_state()
            law_page.wait_for_selector(".texto.int-links", timeout=5_000)

            # get law content
            content = law_page.locator(".texto.int-links").inner_text()

            # close the browser
            browser.close()

            return content
    
    def run_scraper(self, law_id) -> None:
        """
        Runs the scraper to fetch the law document.

        Args:
            law_id (str): ID of the law to fetch.
        """
        with sync_playwright() as playwright:
            content = self.fetch_law_doc(playwright, law_id)
            return content
        
if __name__ == "__main__":
    pass