from pages.base_page import BasePage


class ExpertLandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "main.page-content"
        self.container = "body.landing-expert"

    _login_button = "a.navbar-btn"
    _email_field = "#login_email"
    _password_field = "#login_password"
    _submit_login_button = "button.btn.btn-primary.btn-block"

    def click_login_link(self):
        self.click_on_element(self._login_button)

    def enter_email_field(self, email_input):
        self.send_key_to_element(self._email_field, email_input)

    def enter_password_field(self, password_input):
        self.send_key_to_element(self._password_field, password_input)

    def click_submit_login_button(self):
        self.click_on_element(self._submit_login_button)
