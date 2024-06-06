from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.NAME, 'search_query')
        self.search_button = (By.ID, 'search-icon-legacy')

    def search(self, text):
        search_input = self.find_element(self.search_box)
        search_input.send_keys(text)
        self.click(self.search_button)

