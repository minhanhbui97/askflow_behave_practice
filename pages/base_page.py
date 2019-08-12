from abc import abstractmethod

import abstract as abstract
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    container = None
    element_in_container = None

    def __init__(self, driver):
        self.driver = driver

    def is_present(self):
        if self.get_element(self.element_in_container) is not None and self.get_element(self.container) is not None:
            print("Element with identifier " + self.element_in_container + " is present in " + self.container)
            return True
        else:
            print("Element with identifier " + self.element_in_container + " is NOT present in " + self.container)
            return False

    def wait_until_presence_of_element_located(self, location, timeout=30):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, location)))

    def wait_until_element_to_be_clickable(self, location, timeout=30):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, location)))

    def get_element(self, location):
        self.wait_until_presence_of_element_located(location)
        return self.driver.find_element_by_css_selector(location)

    def click_on_element(self, location):
        self.wait_until_element_to_be_clickable(location)
        self.get_element(location).click()

    def send_key_to_element(self, location, field_input):
        self.wait_until_presence_of_element_located(location)
        self.get_element(location).send_keys(field_input)

    def click_and_confirm_click_element(self, location_element1, location_element2):
        self.click_on_element(location_element1)
        self.click_on_element(location_element2)
