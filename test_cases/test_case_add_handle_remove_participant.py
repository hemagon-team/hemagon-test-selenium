import os
import json
import pytest
from tests import test_organizer_page, test_tournament_page
from pages.login_page import LoginPage

# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Set data
# CHANGE TO SPECIFIC DATA FOR THIS TEST CASE
with open('../data/tournaments/pools-with-finals.json', 'r') as f:
    data = json.load(f)

class TestAddHandleRemoveParticipant:
    @pytest.fixture(autouse=True)
    def set_attributes(self):
        self.create_tournament = test_organizer_page.TestUserCanCreateTournament()
        self.modify_tournament = test_tournament_page.TestUserCanModifyTournament()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        login_page.should_be_authorized_user()
        page.close_cookies()

    def test_add_handle_remove_participants(self, browser):
        self.create_tournament.test_user_can_create_tournament(browser, data)
        self.create_tournament.test_user_can_open_tournament(browser, data)
        self.modify_tournament.test_user_can_create_nomination(browser, data)
        self.modify_tournament.test_user_can_open_registration(browser)
        self.modify_tournament.test_user_can_register_for_the_tournament(browser)
        self.modify_tournament.test_user_can_change_application(browser)
        self.create_tournament.test_user_can_open_tournament(browser, data)
        self.modify_tournament.test_user_can_handle_participants(browser)
        self.modify_tournament.test_user_can_delete_nomination(browser)
        self.create_tournament.test_user_can_delete_tournament(browser, data)
