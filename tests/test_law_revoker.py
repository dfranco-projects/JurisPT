import json
from src.legal_crawler.crawler import LawCrawler

def test_revoked_law_updates_metadata():
    """
    Test that the metadata file is updated correctly when a law is revoked.
    """
    crawler = LawCrawler()
    law_id = "Lei n.º 67/98"
    _, laws_metadata = crawler.run_test_scraper(law_id)
    law = next(l for l in laws_metadata if l["law_id"] == law_id)
    
    assert law["active"] is False