import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.home_page import HomePage
from page.search_results_page import SearchResultsPage
from utils.browser import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.mark.parametrize("search_term, expected_in_title", [
    ("Selenium testing", "Selenium"),
    ("Python tutorials", "Python"),
    ("QA Automation", "Automation")
])
def test_youtube_search_multiple_params(driver, search_term, expected_in_title):
    driver.get("https://www.youtube.com")
    home_page = HomePage(driver)
    home_page.search(search_term)
    results_page = SearchResultsPage(driver)

    wait = WebDriverWait(driver, 20)
    video_titles = wait.until(EC.presence_of_all_elements_located((By.ID, 'video-title')))

    assert len(video_titles) > 0, f"No results found for {search_term}"
    assert expected_in_title in driver.title, f"Expected '{expected_in_title}' to be in the title"
