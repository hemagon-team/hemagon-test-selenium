import os
import json
import pytest
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.stages_page import StagesPage
from pages.organizer_page import OrganizerPage
from pages.locators import TournamentPageLocators


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set user data (modify in data.json)
with open("data.json", "r") as f:
    data = json.load(f)


class TestRunningTournamentWithPools:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        # Close cookies
        page.close_cookies()

    def test_user_can_run_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.open_tournament(data["title"])

        page.click_button(TournamentPageLocators.NOMINATIONS_TAB)
        page.click_button(TournamentPageLocators.NOMINATION_LINK)
        page.click_button(TournamentPageLocators.STAGES_TAB)

        stage = StagesPage(browser, link)
        stage.pools_running()
        stage.playoff_create()
        stage.playoff_running()


if __name__ == "__main__":
    pass
