import pytest
import os
from tests import test_main_page
from pages.login_page import LoginPage


# Set links
base_link = os.environ["TEST_BASEURL"]

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]


class TestCreateRunDeleteTournament:
    @pytest.fixture(autouse=True)
    def set_attributes(self):
        self.main_page = test_main_page.TestUserCanGoToDifferentPagesFromMainPage()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        login_page.should_be_authorized_user()
        page.close_cookies()

    def test_main_page_check(self, browser):
        self.main_page.test_user_can_go_to_profile_page(browser)
        self.main_page.test_user_can_go_to_organizer_page(browser)
        self.main_page.test_user_can_open_tournaments_tab(browser)
        self.main_page.test_user_can_open_rating_tab(browser)
        self.main_page.test_user_can_open_achievements_tab(browser)
        self.main_page.test_user_can_open_about_tab(browser)
        self.main_page.test_user_can_open_contact_tab(browser)
        self.main_page.test_user_can_open_rating_weapon_tabs(browser)
        self.main_page.test_user_can_open_rating_weapon_lists(browser)
        self.main_page.test_user_can_open_about_rating(browser)
        self.main_page.test_user_can_open_import_rating(browser)
        self.main_page.test_user_can_open_instant_fight(browser)
        self.main_page.test_user_can_close_instant_fight(browser)
