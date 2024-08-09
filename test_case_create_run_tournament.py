import pytest
import os
import json
import test_organizer_page
import test_tournament_page
import test_pools_running
import test_finals_running
import test_swiss
from pages.login_page import LoginPage


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set user data (modify in data.json)
with open("data.json", "r") as f:
    data = json.load(f)


class TestCreateRunDeleteTournament:
    @pytest.fixture(autouse=True)
    def set_attributes(self):
        self.create_tournament = test_organizer_page.TestUserCanCreateTournament()
        self.modify_tournament = test_tournament_page.TestUserCanModifyTournament()
        self.run_pools = test_pools_running.TestRunningPools()
        self.run_playoff = test_finals_running.TestRunningPlayoff()
        self.run_swiss = test_swiss.TestRunningSwissSystem()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        login_page.should_be_authorized_user()
        page.close_cookies()

    def test_create_run_delete_tournament(self, browser):
        for dataset in data:
            self.create_tournament.test_user_can_create_tournament(browser, dataset)
            self.create_tournament.test_user_can_open_tournament(browser, dataset)
            self.modify_tournament.test_user_can_open_registration(browser)
            self.modify_tournament.test_user_can_create_nomination(browser, dataset)
            self.modify_tournament.test_user_can_register_for_the_tournament(browser)
            self.modify_tournament.test_user_can_change_application(browser)
            self.create_tournament.test_user_can_open_tournament(browser, dataset)
            self.modify_tournament.test_user_can_add_participants(browser, dataset)
            self.modify_tournament.test_user_can_create_ring(browser, dataset)

            if dataset["type_id"] == 1:
                self.modify_tournament.test_user_can_create_pools_stage(browser, dataset)
                self.modify_tournament.test_user_can_create_pools(browser, dataset)
                self.modify_tournament.test_user_can_add_participants_to_pool(browser)
                self.modify_tournament.test_user_can_set_ring_for_pool(browser)
                self.run_pools.test_user_can_run_pools_stage(browser, full_mode=False)

                if dataset["go_next_stage"]:
                    self.modify_tournament.test_user_can_create_playoff_stage(browser, dataset)
                    self.run_playoff.test_user_can_run_finals_stage(browser, full_mode=False)
                    self.modify_tournament.test_user_can_delete_playoffs(browser, dataset)
                    self.modify_tournament.test_user_can_delete_playoff_stage(browser)

                self.modify_tournament.test_user_can_delete_pools(browser, dataset)
                self.modify_tournament.test_user_can_delete_pools_stage(browser)

            if dataset["type_id"] == 3:
                self.modify_tournament.test_user_can_create_swiss_stage(browser, dataset)
                self.modify_tournament.test_user_can_add_participants_to_swiss(browser)
                self.modify_tournament.test_user_can_set_ring_for_swiss_round(browser)
                self.modify_tournament.test_user_can_set_pairs_for_swiss_round(browser)
                self.run_swiss.test_user_can_run_swiss_stage(browser, full_mode=False)

                if dataset["go_next_stage"]:
                    self.modify_tournament.test_user_can_create_playoff_stage(browser, dataset)
                    self.run_playoff.test_user_can_run_finals_stage(browser, full_mode=False)
                    self.modify_tournament.test_user_can_delete_playoffs(browser, dataset)
                    self.modify_tournament.test_user_can_delete_playoff_stage(browser)

                self.modify_tournament.test_user_can_delete_swiss_rounds(browser)
                self.modify_tournament.test_user_can_delete_pools_stage(browser)

            self.modify_tournament.test_user_can_delete_nomination(browser)
            self.modify_tournament.test_user_can_delete_ring(browser)
            self.create_tournament.test_user_can_delete_tournament(browser, dataset)
