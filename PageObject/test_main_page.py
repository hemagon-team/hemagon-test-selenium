import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.organizer_page import OrganizerPage

link = "https://hemagon.com/"
login_link = "https://hemagon.com/login"
test_email = "paulus.mair@mailfence.com"
test_password = "HEMAhuema@1"


def test_guest_can_go_to_login_page_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    # assert that login page is correct


class TestUserCanGoToOrganizerPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        page.login_user(test_email, test_password)
        time.sleep(1)
        # assert authorized user

    def test_user_can_go_to_organizer_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_organizer_page()
        organizer_page = OrganizerPage(browser, browser.current_url)
        # assert that organizer page is correct
