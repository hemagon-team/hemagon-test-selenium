import os
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.stages_page import StagesPage


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

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
    # Close cookies
    page.close_cookies()


class TestRunningPlayoff:
    def test_user_can_run_finals_stage(self, browser, full_mode=True):
        stage = StagesPage(browser, browser.current_url)
        stage.playoff_create()
        stage.playoff_running(full_mode)
