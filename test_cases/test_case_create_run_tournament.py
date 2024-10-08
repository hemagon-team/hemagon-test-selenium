import pytest
import os
import json
from tests import test_finals_running, test_swiss, test_organizer_page, test_pools_running, test_tournament_page
from pages.login_page import LoginPage


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set data
DATA_DIR = "../data/tournaments/"

FILENAMES = [
    "pools-with-finals.json",
    "pools-without-finals.json",
    "swiss-with-finals.json",
    "swiss-without-finals.json",
    "pools-tiny-odd.json",
    "pools-small-standard.json",
    "pools-small-odd.json",
    "pools-medium-standard.json",
    "pools-medium-odd.json",
    "pools-large-standard.json",
    "pools-large-odd.json",
    "swiss-without-finals-odd.json"
]

def pytest_generate_tests(metafunc):
    if "data" in metafunc.fixturenames:
        data = []
        for filename in FILENAMES:
            with open(os.path.join(DATA_DIR, filename)) as f:
                dataset = json.load(f)
                data.append(dataset)
        metafunc.parametrize("data", data)


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

    def test_create_run_delete_tournament(self, browser, data):
        self.create_tournament.test_user_can_create_tournament(browser, data)
        self.create_tournament.test_user_can_open_tournament(browser, data)

        for ring_data in data["rings"]:
            self.modify_tournament.test_user_can_create_ring(browser, ring_data)

        for nomination_data in data["nominations"]:
            self.modify_tournament.test_user_can_create_nomination(browser, nomination_data)
            self.modify_tournament.test_user_can_add_participants(browser, nomination_data)

            for stage_data in nomination_data["stages"]:

                if stage_data["type"] == "pools":
                    self.modify_tournament.test_user_can_create_pools_stage(browser, stage_data)
                    self.modify_tournament.test_user_can_create_pools(browser, stage_data)
                    self.modify_tournament.test_user_can_add_participants_to_pool(browser)
                    self.modify_tournament.test_user_can_set_ring_for_pool(browser)
                    self.run_pools.test_user_can_run_pools_stage(browser, full_mode=False)

                if stage_data["type"] == "playoff":
                    self.modify_tournament.test_user_can_create_playoff_stage(browser, stage_data)
                    self.run_playoff.test_user_can_run_finals_stage(browser, full_mode=False)

                if stage_data["type"] == "swiss system":
                    self.modify_tournament.test_user_can_create_swiss_stage(browser, stage_data)
                    self.modify_tournament.test_user_can_add_participants_to_swiss(browser)
                    self.modify_tournament.test_user_can_set_ring_for_swiss_round(browser)
                    self.modify_tournament.test_user_can_set_pairs_for_swiss_round(browser)
                    self.run_swiss.test_user_can_run_swiss_stage(browser, full_mode=False)

            self.modify_tournament.test_should_be_correct_nominations(browser, data)
            self.create_tournament.test_user_can_open_tournament(browser, data)

            for stage_data in nomination_data["stages"]:
                if stage_data["type"] == "pools":
                    self.modify_tournament.test_user_can_delete_pools(browser, stage_data)
                    self.modify_tournament.test_user_can_delete_pools_stage(browser)
                if stage_data["type"] == "playoff":
                    self.modify_tournament.test_user_can_delete_playoffs(browser, stage_data)
                    self.modify_tournament.test_user_can_delete_playoff_stage(browser)
                if stage_data["type"] == "swiss system":
                    self.modify_tournament.test_user_can_delete_swiss_rounds(browser, stage_number=stage_data["stage_number"])
                    self.modify_tournament.test_user_can_delete_pools_stage(browser)
            self.modify_tournament.test_should_be_no_stages_title(browser)

            self.modify_tournament.test_user_can_delete_nomination(browser)

            print("Finished test case", data["title"])

        self.modify_tournament.test_user_can_delete_ring(browser)
        self.create_tournament.test_user_can_delete_tournament(browser, data)
