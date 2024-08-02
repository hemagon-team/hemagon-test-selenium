import os
import json
import pytest
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.stages_page import StagesPage
from pages.organizer_page import OrganizerPage
from pages.locators import TournamentPageLocators
import time


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set user data (modify in data.json)
"""with open("data.json", "r") as f:
    data = json.load(f)"""


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


class TestRunningTournamentSwissSystem:
    def test_user_can_run_tournament(self, browser, data, full_mode=True):
        page = OrganizerPage(browser, link)
        page.open()
        page.open_tournament(data["title"])

        page.click_button(TournamentPageLocators.NOMINATIONS_TAB)
        page.click_button(TournamentPageLocators.NOMINATION_LINK)
        page.click_button(TournamentPageLocators.STAGES_TAB)
        time.sleep(0.3)

        stage = StagesPage(browser, link)
        if full_mode:
            stage.check_fight_swiss_buttons()
        time.sleep(0.3)
        stage.swiss_running(full_mode)
