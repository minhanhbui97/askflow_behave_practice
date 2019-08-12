from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time


class AskerWorkspace(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = self._chat_area
        self.container = "div.gi-Layout.gi-Workspace"

    _chat_area = "textarea.ex-richeditor"

    def send_chat_message(self, message):
        chat_message = self.get_element(self._chat_area)
        time.sleep(2)
        chat_message.send_keys(message)
        chat_message.send_keys(Keys.ENTER)
