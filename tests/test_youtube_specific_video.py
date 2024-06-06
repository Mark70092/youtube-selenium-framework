import pytest
from selenium import webdriver
from utils.browser import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_youtube_specific_video(driver):
    driver.get("https://www.youtube.com")

    search_box = driver.find_element_by_xpath('//input[@id="search"]')
    search_box.send_keys("Selenium tutorial for beginners")
    search_button = driver.find_element_by_xpath('//button[@id="search-icon-legacy"]')
    search_button.click()
    
    driver.implicitly_wait(10)
    
    video_title_xpath = '//a[@title="Selenium Full Course - Learn Selenium in 12 Hours | Selenium Tutorial | Edureka"]'
    specific_video = driver.find_element_by_xpath(video_title_xpath)
    
    assert specific_video is not None, "Specific video not found in search results"
    specific_video.click()
    
    driver.implicitly_wait(10)
    
    assert "Selenium Full Course" in driver.title, "Video page did not load correctly"

