from webscraping.law_scraper import LawScraper

def test_revoked_law_updates():
    """
    Test that the metadata file is updated correctly when a law is revoked.
    """
    scraper = LawScraper()

    # This is a test case where the law is known to be revoked but the scraper does not know it yet
    law_id = "Lei n.º 67/98"
    laws_metadata = [{
        "law_id": "Lei n.º 67/98",
        "subject": "Transpõe a Diretiva da UE sobre proteção de dados pessoais (revogada, mas importante historicamente).",
        "active": True
    }]

    # Simulate the law being revoked (in-memory)
    _, updated_metadata = scraper.run_test_scraper(law_id=law_id, laws_metadata=laws_metadata)
    law = next(l for l in updated_metadata if l["law_id"] == law_id)
    
    assert law["active"] is False