from pages.base_page import BasePage


class ExpertWorkspace(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = self._chat_area
        self.container = "div.gi-Layout.gi-Workspace"

    _chat_area = "textarea.ex-richeditor"
    _chat_received = ".chat-message"

    def get_asker_last_message(self, message):
        chat_sent = self.get_element(self._chat_received)
        if chat_sent.text == message:
            pass
