import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page.home_page import HomePage
from page.search_results_page import SearchResultsPage
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

    wait = WebDriverWait(driver, 20)
    results_page = SearchResultsPage(driver)

    try:
        # Checking for the presence of the specified element.
        # If this element is found, the test fails.
        invalid_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="contents"]/ytd-background-promo-renderer/yt-icon/yt-icon-shape/icon-shape/div'))
        )
    except TimeoutException:
        invalid_element = None

        # This test verifies that YouTube returns results even for nonsensical search queries.
        # The test passes if the specified element is not found on the page.
    assert invalid_element is None, "Invalid element found on the page, test failed"
