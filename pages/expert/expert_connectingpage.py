import time
from pages.base_page import BasePage


class ExpertConnectingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "div.waiting-question"
        self.container = "div.gi-WorkspaceConnectingArea"

    _bid_question_description = "div.gi-BiddingQuestionInfo-text"
    _skip_button = "#skip-button"
    _confirm_skip_button = "#confirm-skip-button"
    _claim_button = "#claim-button"
    _confirm_claim_button = "#confirm-claim-button"

    def click_claim_asker_question(self, question):
        while True:
            if self.get_element(self._bid_question_description).text is not None:
                print(self.get_element(self._bid_question_description).text)
                if self.get_element(self._bid_question_description).text == question:
                    self.click_on_element(self._claim_button)
                    self.click_on_element(self._confirm_claim_button)
                    time.sleep(1)
                    break
                else:
                    self.click_on_element(self._skip_button)
                    self.click_on_element(self._confirm_skip_button)
            time.sleep(1)

