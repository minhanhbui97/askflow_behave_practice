from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time


class ProblemExpertIntroModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "button.gi-Button--primary"
        self.container = "#modal-problem-expert-intro"

    def close_expert_intro_modal(self):
        if self.get_element(self.element_in_container) is not None:
            self.click_on_element(self.element_in_container)
