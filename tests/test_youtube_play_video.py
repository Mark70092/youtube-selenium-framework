import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.browser import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_youtube_play_video(driver):
    driver.get("https://www.youtube.com")
    
    search_box = driver.find_element(By.XPATH, '//input[@id="search"]')
    search_box.send_keys("Selenium tutorial for beginners")
    search_button = driver.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
    search_button.click()
    
    driver.implicitly_wait(10)
    
    video_title_xpath = '//a[@title="Selenium Full Course - Learn Selenium in 12 Hours | Selenium Tutorial | Edureka"]'
    specific_video = driver.find_element(By.XPATH, video_title_xpath)
    specific_video.click()
    
    driver.implicitly_wait(10)
    
    play_button = driver.find_element(By.XPATH, '//button[@class="ytp-play-button ytp-button"]')
    play_button.click()
    
    video_player = driver.find_element(By.XPATH, '//video[@class="video-stream html5-main-video"]')
    assert video_player.get_attribute("paused") == "false", "Video is not playing"
