import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.browser import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_youtube_invalid_search(driver):
    driver.get("https://www.youtube.com")
    home_page = HomePage(driver)
    home_page.search("asffojhwewijbgqwqpuigbpquwiebphiwfQFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFebfhipwebweibvewvweib")
    results_page = SearchResultsPage(driver)
    assert len(results_page.get_video_titles()) == 0  # Ожидаем, что не будет результатов
