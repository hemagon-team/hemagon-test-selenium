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
data = []
with open('data/tournaments/pools-with-finals.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/pools-without-finals.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/swiss-with-finals.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/swiss-without-finals.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/pools-tiny-odd.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/pools-small-standard.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/pools-small-odd.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/pools-medium-standard.json', 'r') as f:
    data.append(json.load(f))
with open('data/tournaments/pools-medium-odd.json', 'r') as f:
    data.append(json.load(f))
# Large tournaments are commented because it's impossible to enroll more than 64 participants, while 80 needed
"""with open('../data/tournaments/pools-large-standard.json', 'r') as f:
    data.append(json.load(f))
with open('../data/tournaments/pools-large-odd.json', 'r') as f:
    data.append(json.load(f))"""
with open('../data/tournaments/swiss-without-finals-odd.json') as f:
    data.append(json.load(f))


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

            for ring_data in dataset["rings"]:
                self.modify_tournament.test_user_can_create_ring(browser, ring_data)

            for nomination_data in dataset["nominations"]:
                self.modify_tournament.test_user_can_create_nomination(browser, nomination_data)
                self.modify_tournament.test_user_can_add_participants(browser, nomination_data)

                for stage_data in nomination_data["stages"]:

                    if stage_data["type_id"] == 1:
                        self.modify_tournament.test_user_can_create_pools_stage(browser, stage_data)
                        self.modify_tournament.test_user_can_create_pools(browser, stage_data)
                        self.modify_tournament.test_user_can_add_participants_to_pool(browser)
                        self.modify_tournament.test_user_can_set_ring_for_pool(browser)
                        self.run_pools.test_user_can_run_pools_stage(browser, full_mode=False, stage_number=stage_data["stage_number"])

                    if stage_data["type_id"] == 2:
                        self.modify_tournament.test_user_can_create_playoff_stage(browser, stage_data)
                        self.run_playoff.test_user_can_run_finals_stage(browser, full_mode=False, stage_number=stage_data["stage_number"])

                    if stage_data["type_id"] == 3:
                        self.modify_tournament.test_user_can_create_swiss_stage(browser, stage_data)
                        self.modify_tournament.test_user_can_add_participants_to_swiss(browser)
                        self.modify_tournament.test_user_can_set_ring_for_swiss_round(browser)
                        self.modify_tournament.test_user_can_set_pairs_for_swiss_round(browser)
                        self.run_swiss.test_user_can_run_swiss_stage(browser, full_mode=False, stage_number=stage_data["stage_number"])

                for stage_data in nomination_data["stages"]:
                    if stage_data["type_id"] == 1:
                        self.modify_tournament.test_user_can_delete_pools(browser, stage_data)
                        self.modify_tournament.test_user_can_delete_pools_stage(browser, stage_number=stage_data["stage_number"])
                    if stage_data["type_id"] == 2:
                        self.modify_tournament.test_user_can_delete_playoffs(browser, stage_data)
                        self.modify_tournament.test_user_can_delete_playoff_stage(browser, stage_number=stage_data["stage_number"])
                    if stage_data["type_id"] == 3:
                        self.modify_tournament.test_user_can_delete_swiss_rounds(browser, stage_number=stage_data["stage_number"])
                        self.modify_tournament.test_user_can_delete_pools_stage(browser, stage_number=stage_data["stage_number"])
                self.modify_tournament.test_should_be_no_stages_title(browser)

                self.modify_tournament.test_user_can_delete_nomination(browser)

                print("Finished test case", dataset["title"])

            self.modify_tournament.test_user_can_delete_ring(browser)
            self.create_tournament.test_user_can_delete_tournament(browser, dataset)
