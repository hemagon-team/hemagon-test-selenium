import os
import pytest
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from pages.login_page import LoginPage

# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/users/april.anna.vas"

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
    page.should_be_authorized_user()
    # Close cookies
    page.close_cookies()


class TestUserCanOpenProfile:
    def test_user_can_open_profile(self, browser):
        page = ProfilePage(browser, link)
        page.open()
        page.should_be_profile_page()

    def test_user_can_see_profile_name(self, browser):
        page = ProfilePage(browser, link)
        page.open()
        page.should_be_user_name()

    def test_user_can_see_profile_club(self, browser):
        page = ProfilePage(browser, link)
        page.open()
        page.should_be_user_club()
