from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.video_titles = (By.ID, 'video-title')

    def get_video_titles(self):
        return [title.text for title in self.find_elements(self.video_titles)]
