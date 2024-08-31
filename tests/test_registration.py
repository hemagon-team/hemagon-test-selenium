import os
import json
import pytest
# from pages.login_page import LoginPage
# from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
# from pages.stages_page import StagesPage
# from pages.organizer_page import OrganizerPage
# from pages.locators import TournamentPageLocators
import time
from selenium.webdriver.common.by import By


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