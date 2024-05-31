import pytest
import os
import test_organizer_page
import test_tournament_page
import test_pools_and_finals_running
from pages.login_page import LoginPage


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]


class TestCreateRunDeleteTournament:
    @pytest.fixture(autouse=True)
    def set_attributes(self):
        self.create_tournament = test_organizer_page.TestUserCanCreateTournament()
        self.modify_tournament = test_tournament_page.TestUserCanModifyTournament()
        self.run_tournament = test_pools_and_finals_running.TestRunningTournamentWithPools()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        login_page.should_be_authorized_user()

    def test_create_run_delete_tournament(self, browser):
        self.create_tournament.test_user_can_create_tournament(browser)
        self.create_tournament.test_user_can_open_tournament(browser)
        self.create_tournament.test_user_can_delete_tournament(browser)
