import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from pages.profile_settings_page import ProfileSettingsPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
import json
import time
from conftest import browser
# version = "128.0.6613.86"
#
# # Path to your custom Chrome binary
# chrome_binary_path = '/home/thatsme/chrome-linux64/chrome'
#
# # Path to the chromedriver executable (note: it's the file, not the directory)
# chrome_driver_path = '/home/thatsme/chromedriver/chromedriver'
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = chrome_binary_path
#
# # Service with correct path to chromedriver
# service = Service(executable_path=chrome_driver_path)
#
# # Initialize the WebDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + '/login'

#Set user
with open("/home/thatsme/git/hemagon-test-selenium/data/other/user_data.json", "r") as f:
    data = json.load(f)
email = data['email']
email1 = data['email1']
password = data['password']


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
        reg.user_can_log_in(email, password)
        #time.sleep(4)

class TestChangingProfile:
    def test_user_can_change_the_profile(self, browser, full_mode=True):
        profchange = ProfileSettingsPage(browser, base_link)
        login_page = LoginPage(browser, browser.current_url)
        reg = RegistrationPage(browser, link)
        login_page.login_user(email, password)
        profchange.open_settings()
        profchange.user_can_change_the_name()
        profchange.user_can_change_the_last_name()
        profchange.user_can_change_the_email()
        profchange.user_can_change_the_country()
        profchange.user_can_change_the_city()
        reg.user_can_log_out()
        login_page.login_user(email1, password)
