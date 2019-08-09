from pages.base_page import BasePage


class ExpertIntroModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.container = "div.gi-IntroContent-container"
        self.element_in_container = "button#js-introSkip"

    def click_skip_button(self):
        if self.get_element(self.element_in_container) is not None:
            self.click_on_element(self.element_in_container)