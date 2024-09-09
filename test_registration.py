import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
import time

version = "128.0.6613.86"

# Path to your custom Chrome binary
chrome_binary_path = '/home/thatsme/chrome-linux64/chrome'

# Path to the chromedriver executable (note: it's the file, not the directory)
chrome_driver_path = '/home/thatsme/chromedriver/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_path

# Service with correct path to chromedriver
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + '/login'

@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.go_to_login_page()
    # Close cookies
    page.close_cookies()

class TestRegistration:

    def test_user_can_register_a_new_account(self, browser, full_mode=True):
        reg = RegistrationPage(browser, link)
        reg.user_can_open_the_registration_form()
        reg.user_can_fill_the_form()
        reg.user_can_update_the_profile()
        time.sleep(1)
        reg.user_can_log_out()
        browser.get(link)
        reg.user_can_log_in()
        time.sleep(4)
