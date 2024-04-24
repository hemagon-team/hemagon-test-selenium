import os
import json
import pytest
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
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

# Calculate pools number based on participants number (from user data)
pools_number = (data["participants_number"] + 7 - 1) // 7


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


class TestUserCanModifyTournament:
    # Not the best way to organize setup
    # THINK OF A BETTER LOGIC
    def test_setup_create_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.create_tournament(data["title"], data["start_date"], data["end_date"],
                               data["country"], data["city"], data["description"])

    def test_user_can_create_nomination(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.create_nomination(data["nomination_title"], data["weapon_id"],
                               data["fight_time"], data["last_round_time"])

    def test_user_can_create_stage(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.create_stage(data["type_id"], data["to_the_finals"], data["fight_time"], data["go_next_stage"])

    def test_user_can_add_participants(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.add_participants(str(data["participants_number"]))

    def test_user_can_create_ring(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.create_ring(data["ring_title"])

    @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_create_pools(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.create_pools(pools_number)

    @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_add_participants_to_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.add_participants_to_pool()

    @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_set_ring_for_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.set_ring_for_pool()

    @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_delete_pools(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.delete_pools(pools_number)

    @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_add_participants_to_swiss(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.add_participants_to_swiss()

    @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_delete_swiss_round(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.delete_swiss()

    @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_set_ring_for_swiss_round(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.set_ring_for_pairs()

    @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_set_ring_for_swiss_round(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.change_pairs()

    def test_user_can_delete_stage(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.delete_stage()

    def test_user_can_delete_nomination(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.delete_nomination()

    def test_user_can_delete_ring(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])
        page = TournamentPage(browser, browser.current_url)
        page.delete_ring()

    # Not the best way to organize teardown
    # THINK OF A BETTER LOGIC
    def test_teardown_delete_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.delete_tournament(data["title"])
