from pages.base_page import BasePage
import time


class AskerLoginModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "button#login-button"
        self.container = "div#modal-login"

    _google_login_button = "#modal-login .gi-Button.gi-Button--Google"
    _google_login_url = "https://accounts.google.com/signin/oauth"
    _gemail_field = "input#identifierId"
    _gemail_submit_button = "div#identifierNext"
    _gpassword_field = "input[type='password]"
    _gpassword_submit_button = "div#passwordNext"

    _email_field = "#modal-login input[type='email']"
    _password_field = "#modal-login input[type='password']"
    _login_submit_button = "button#login-button"

    def click_google_login_button(self):
        self.click_on_element(self._google_login_button)

    def switch_to_google_browser(self, email, password):
        parent_window = self.driver.current_window_handle
        self.click_google_login_button()
        list_window_handles = self.driver.window_handles

        for window_handle in list_window_handles:
            self.driver.switch_to_window(window_handle)
            if self._google_login_url in self.driver.current_url:
                time.sleep(3)
                self.enter_gemail_field(email)
                self.click_submit_email_button()
                time.sleep(5)
                self.enter_gpassword_field(password)
                self.click_submit_password_button()
                break

    def enter_gemail_field(self, email_input):
        self.send_key_to_element(self._gemail_field, email_input)

    def click_submit_email_button(self):
        self.click_on_element(self._gemail_submit_button)

    def enter_gpassword_field(self, password_input):
        self.send_key_to_element(self._gemail_field, password_input)

    def click_submit_password_button(self):
        self.click_on_element(self._gpassword_submit_button)

    def enter_email_field(self, email_input):
        self.send_key_to_element(self._email_field, email_input)

    def enter_password_field(self, password_input):
        self.send_key_to_element(self._password_field, password_input)

    def click_submit_login_button(self):
        self.click_on_element(self._login_submit_button)