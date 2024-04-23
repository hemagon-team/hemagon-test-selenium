import os
import time
import pytest
import json
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.organizer_page import OrganizerPage

link = os.environ["TEST_BASEURL"]

# Set user data (modify in data.json)
with open("data.json", "r") as f:
    data = json.load(f)


def test_guest_can_go_to_login_page_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(1)
    login_page.should_be_login_page()


class TestUserCanGoToOrganizerPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(data["test_email"], data["test_password"])
        time.sleep(1)
        login_page.should_be_authorized_user()

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

    def test_user_can_open_fighters_tab(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_fighters_tab()

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

    def test_user_can_open_longsword_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_longsword()

    def test_user_can_open_saber_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_saber()

    def test_user_can_open_rapier_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_rapier()

    def test_user_can_open_rapier_dagger_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_rapier_dagger()

    def test_user_can_open_dussak_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_dussak()

    def test_user_can_open_spear_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_spear()

    def test_user_can_open_sword_buckler_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_sword_buckler()

    def test_user_can_open_sidesword_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_sidesword()

    def test_user_can_open_triathlon_rating(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.open_rating_triathlon()
