import os
import pytest

from conftest import browser
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_settings_page import ProfileSettingsPage
import time

# Set links
base_link = os.environ["TEST_BASEURL"]

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_user(email, password)
    time.sleep(2)
    # Close cookies
    page.close_cookies()


class TestChangingProfile:

    # def test_user_can_change_the_name(self, browser, full_mode=True):
    #     profchange = ProfileSettingsPage(browser, base_link)
    #     profchange.open_settings()
    #     profchange.user_can_change_the_name()
    #     time.sleep(2)
    #
    # def test_user_can_change_the_last_name(self, browser, full_mode=True):
    #     profchange = ProfileSettingsPage(browser, base_link)
    #     profchange.open_settings()
    #     profchange.user_can_change_the_last_name()
    #
    # def test_user_can_change_the_country(self, browser, full_mode=True):
    #     profchange = ProfileSettingsPage(browser, base_link)
    #     profchange.open_settings()
    #     profchange.user_can_change_the_country()
    # def test_user_can_set_the_club(self, browser, full_mode=True):
    #     profchange = ProfileSettingsPage(browser, base_link)
    #     profchange.open_settings()
    #     profchange.user_can_set_the_club()
    #
    # def test_user_can_change_the_club(self, browser, full_mode=True):
    #     profchange = ProfileSettingsPage(browser, base_link)
    #     profchange.open_settings()
    #     profchange.user_can_change_the_club()

    def test_user_can_remove_the_club(self, browser, full_mode=True):
        profchange = ProfileSettingsPage(browser, base_link)
        profchange.open_settings()
        profchange.user_can_remove_the_club()
