from pages.base_page import BasePage


class AskerLandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "div.gi-VcDemoAskBox"
        self.container = "div.gi-Layout.gi-Landing--QueryV2"

    _login_button = "#test-login-button"
    _asker_login_modal = "#modal-login"

    def click_login_link(self):
        self.click_on_element(self._login_button)
