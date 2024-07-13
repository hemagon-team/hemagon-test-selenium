import os
import time
import pytest
import json
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.organizer_page import OrganizerPage
from pages.profile_page import ProfilePage

link = os.environ["TEST_BASEURL"]

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set user data (modify in data.json)
with open("data.json", "r") as f:
    data = json.load(f)


class TestGuestCanGoToDifferentPagesFromMainPage:
    # Add more functions and inherit to User class
    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        time.sleep(1)
        login_page.should_be_login_page()


class TestUserCanGoToDifferentPagesFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        time.sleep(1)
        login_page.should_be_authorized_user()
        # Close cookies
        page.close_cookies()

    @pytest.mark.issue
    def test_user_can_go_to_profile_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_profile()
        profile_page = ProfilePage(browser, browser.current_url)
        time.sleep(1)
        profile_page.should_be_profile_page()

    @pytest.mark.issue
    def test_user_can_go_to_organizer_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_organizer_page()
        organizer_page = OrganizerPage(browser, browser.current_url)
        time.sleep(1)
        organizer_page.should_be_organizer_url()

    def test_user_can_open_tournaments_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_tournaments_tab()

    def test_user_can_open_rating_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_tab()

    @pytest.mark.skip(reason="No tab on the website now")
    def test_user_can_open_fighters_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_fighters_tab()

    @pytest.mark.skip(reason="No tab on the website now")
    def test_user_can_open_clubs_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_clubs_tab()

    def test_user_can_open_achievements_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_achievements_tab()

    def test_user_can_open_about_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_about_tab()

    def test_user_can_open_contact_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_contact_tab()

    def test_user_can_open_rating_weapon_tabs(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_for_every_weapon()

    def test_user_can_open_rating_weapon_lists(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_overall_list_for_every_weapon()

    def test_user_can_open_about_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_about()

    def test_user_can_open_import_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_import()

    # I don't know where are these functions
    """def test_user_can_open_contact_tab_from_footer(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_contact_tab_from_footer()

    def test_user_can_open_about_tab_from_footer(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_about_tab_from_footer()

    def test_user_can_open_terms_and_privacy_from_footer(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_terms_and_privacy_from_footer()"""

    def test_user_can_open_instant_fight(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_instant_fight()

    def test_user_can_close_instant_fight(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.close_instant_fight()
