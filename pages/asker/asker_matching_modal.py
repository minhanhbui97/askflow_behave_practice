from pages.base_page import BasePage


class AskerMatchingModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "h4.modal-title"
        self.container = "#modal-expert-matching"
