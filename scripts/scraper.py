from playwright.sync_api import sync_playwright

class LawScraper:
    def __init__(self):
        self.url = "https://diariodarepublica.pt"

    def fetch_law_document(self, law_id):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # open search page
            page.goto(f"{self.url}/dr/pesquisa")

            # search by law id
            page.fill('input[placeholder="Pesquisar"]', law_id)
            page.keyboard.press('Enter')

            # wait until results load
            page.wait_for_selector('a.title')

            # open first result
            page.click('a.title')
            page.wait_for_load_state('networkidle')

            # get rendered html
            content = page.content()
            browser.close()

            print(f"[✓] fetched document for {law_id}")
            return content
        
if __name__ == "__main__":

    scraper = LawScraper()
    html = scraper.fetch_law_document("Decreto-Lei n.º 90-C/2022")
    print(html[:1500])