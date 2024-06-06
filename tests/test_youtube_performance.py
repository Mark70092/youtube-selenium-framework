import pytest
import time
from selenium import webdriver
from utils.browser import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_youtube_performance(driver):
    start_time = time.time()
    driver.get("https://www.youtube.com")
    load_time = time.time() - start_time
    assert load_time < 5
