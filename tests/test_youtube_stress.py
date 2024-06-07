import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import get_driver
from threading import Thread

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def perform_search(driver, query):
    driver.get("https://www.youtube.com")
    search_box = driver.find_element(By.XPATH, '//input[@id="search"]')
    search_box.send_keys(query)
    search_button = driver.find_element(By.XPATH, '//button[@id="search-icon-legacy"]')
    search_button.click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'video-title')))

def test_stress_search():
    queries = ["Selenium tutorial", "Python tutorial", "QA Automation", "Tech news", "Music videos"]
    threads = []
    for query in queries:
        driver = get_driver()
        t = Thread(target=perform_search, args=(driver, query))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
