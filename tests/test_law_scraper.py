from webscraping.law_scraper import LawScraper

def test_law_scraper_dl_90_2022() -> None:
    """
    Test the output of the law scraper for Decreto-Lei n.º 90-C/2022.
    """
    scraper = LawScraper()
    content, _ = scraper.run_test_scraper("Decreto-Lei n.º 90-C/2022")

    assert "Decreto-Lei n.º 90-C/2022" in content
    assert "programa Porta 65" in content
    assert "Instituto da Habitação e da Reabilitação Urbana (IHRU)" in content
    assert "no âmbito do Programa de Apoio ao Arrendamento têm prazo mínimo de cinco anos" in content

def test_law_scraper_lei_37_2025() -> None:
    """
    Test the output of the law scraper for Lei n.º 37/2025.
    """
    scraper = LawScraper()
    content, _ = scraper.run_test_scraper("Lei n.º 37/2025")

    assert "Lei n.º 37/2025" in content
    assert "Alteração à lei de proteção de crianças e jovens em perigo" in content
    assert "Manter contacto com a criança e jovem após a cessação" in content

def test_law_scraper_dl_446_85() -> None:
    """
    Test the output of the law scraper for Decreto-Lei n.º 446/85.
    """
    scraper = LawScraper()
    content, _ = scraper.run_test_scraper("Decreto-Lei n.º 446/85")

    assert "Decreto-Lei n.º 446/85" in content
    assert "celeridade e de precisão, a existência de monopólios, oligopólios" in content
    assert "desequilíbrio de prestações gravemente atentatório da boa-fé" in content
    assert "inobservância do preceituado no n.º 1" in content
