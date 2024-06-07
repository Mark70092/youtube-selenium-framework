import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

    wait = WebDriverWait(driver, 30)  # Увеличьте время ожидания до 30 секунд

    video_title_xpath = '//a[@title="Selenium Full Course - Learn Selenium in 12 Hours | Selenium Tutorial For Beginners | Edureka"]'
    try:
        specific_video = wait.until(EC.presence_of_element_located((By.XPATH, video_title_xpath)))
        assert specific_video is not None, "Expected video not found in search results"
        specific_video.click()

        # Ждем загрузки страницы видео
        wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), 'Selenium Full Course - Learn Selenium in 12 Hours | Selenium Tutorial For Beginners | Edureka')]")))

        # Проверка наличия заданного текста на странице
        assert driver.find_element(By.XPATH, f"//*[contains(text(), 'Selenium Full Course - Learn Selenium in 12 Hours | Selenium Tutorial For Beginners | Edureka')]") is not None, "Expected video title not found on page"

    except TimeoutException:
        assert False, "Timed out waiting for video to play"
