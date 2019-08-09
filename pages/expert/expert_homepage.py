from pages.base_page import BasePage


class ExpertHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.container = "div.expert-home-main"
        self.element_in_container = "div.expert-primary-menu a.link-item.btn"

    _start_working_button = "div.expert-primary-menu a.link-item.btn"

    def click_on_start_working_button(self):
        self.click_on_element(self._start_working_button)
