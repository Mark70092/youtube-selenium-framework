import pytest
from selenium import webdriver
from utils.browser import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_youtube_home_videos(driver):
    driver.get("https://www.youtube.com")
    video_elements = driver.find_elements_by_id('video-title')
    assert len(video_elements) > 0
