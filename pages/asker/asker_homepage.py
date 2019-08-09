from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class AskerHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_in_container = "a#setting_menu"
        self.container = "div.gi-navBar"

    _url_text = "home"
    _question_description_field = ".gi-FormGroup textarea.gi-Input"
    _question_type_select = "select.gi-InputCustomSelect"
    _post_question_button = "button.gi-Button"

    def enter_question_description_field(self, question_input):
        self.send_key_to_element(self._question_description_field, question_input)

    def select_question_type(self, type_input):
        question_type_list = self.get_element(self._question_type_select)
        select_type = Select(question_type_list)
        select_type.select_by_value(type_input)

    def click_on_submit_question_button(self):
        self.click_on_element(self._post_question_button)
