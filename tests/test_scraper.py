import pytest
from scraper import LawScraper

def test_law_scraper_output() -> None:
    """
    Test the output of the law scraper for Decreto-Lei n.º 90-C/2022.
    """
    scraper = LawScraper()
    content = scraper.run_scraper( "Decreto-Lei n.º 90-C/2022")

    with open("/tmp/test_scraper_decreto_lei_90C_22.txt", "w", encoding="utf-8") as f:
        f.write(content)

    assert "Decreto-Lei n.º 90-C/2022" in content
    assert "programa Porta 65" in content
    assert "Instituto da Habitação e da Reabilitação Urbana (IHRU)" in content
    assert "no âmbito do Programa de Apoio ao Arrendamento têm prazo mínimo de cinco anos" in content

def test_law_scraper_lei_37_2025() -> None:
    """
    Test the output of the law scraper for Lei n.º 37/2025.
    """
    scraper = LawScraper()
    content = scraper.run_scraper("Lei n.º 37/2025")

    with open("/tmp/test_scraper_lei_37_25.txt", "w", encoding="utf-8") as f:
        f.write(content)

    assert "Lei n.º 37/2025" in content
    assert "Alteração à lei de proteção de crianças e jovens em perigo" in content
    assert "Manter contacto com a criança e jovem após a cessação" in content