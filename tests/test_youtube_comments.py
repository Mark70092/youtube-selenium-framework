import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browser import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_youtube_comments(driver):
    video_url = "https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&ab_channel=TechWithTim"
    driver.get(video_url)

    # Ожидание загрузки комментариев
    driver.implicitly_wait(10)

    # Проверка наличия секции комментариев
    comments_section = driver.find_element(By.XPATH, '//*[@id="comments"]')
    assert comments_section is not None
