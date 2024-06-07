import pytest
from selenium import webdriver
from page.home_page import HomePage
from utils.browser import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_youtube_navigation(driver):
    driver.get("https://www.youtube.com")
    assert "YouTube" in driver.title
