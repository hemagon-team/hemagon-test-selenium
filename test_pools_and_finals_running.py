import os
import json
import pytest
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.stages_page import StagesPage
from pages.organizer_page import OrganizerPage


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set user data (modify in data.json)
with open("data.json", "r") as f:
    data = json.load(f)

@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_user(email, password)
    # Close cookies
    page.close_cookies()

class TestRunningTournamentWithPools:
    def TestUserCanRunTournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.open_tournament(data["title"])

        self.click_button(TournamentPageLocators.NOMINATIONS_TAB)
        self.click_button(TournamentPageLocators.NOMINATION_LINK)
        self.click_button(TournamentPageLocators.STAGES_TAB)

        StagesPage.pools_running(self)
        StagesPage.playoff_create(self)
        StagesPage.playoff_running(self)       