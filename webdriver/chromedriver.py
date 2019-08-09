import os
from selenium import webdriver


def set_chrome_options(headless_mode=False):
    headless_option = webdriver.ChromeOptions()
    if headless_mode:
        headless_option.add_argument('headless')
        headless_option.add_argument('--window-size=1920x1080')
    return headless_option


def get_driver(headless_mode=False):
    script_dir = os.path.dirname(os.path.realpath('__file__'))
    rel_path = "/webdriver/chromedriver"
    driver_location = script_dir + rel_path
    os.environ["webdriver.chrome.driver"] = driver_location
    chrome_options = set_chrome_options(headless_mode)
    driver = webdriver.Chrome(driver_location, chrome_options=chrome_options)
    driver.implicitly_wait(10)
    return driver
