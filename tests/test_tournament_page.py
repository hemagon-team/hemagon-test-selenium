import os
import pytest
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage

# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Currently not runnable, can only be used as a part of test case


class TestUserCanModifyTournament:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        page.should_be_authorized_user()
        # Close cookies
        page.close_cookies()

    def test_user_can_create_nomination(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.create_nomination(data["nomination_title"], data["weapon_id"],
                               data["fight_time"], data["last_round_time"])

    def test_user_can_create_pools_stage(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.create_stage(type_id=data["type_id"], fight_time=data["stage_fight_time"],
                          go_next_stage=data["go_next_stage"])

    def test_user_can_create_swiss_stage(self, browser, data):
        page = TournamentPage(browser, browser.current_url)
        page.create_stage(data["type_id"], data["fight_time"], data["go_next_stage"],
                          swiss_empty_win=data["swiss_empty_win"], swiss_win_points=data["swiss_empty_points"])

    def test_user_can_add_participants(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.add_participants(str(data["participants_number"]))

    def test_user_can_create_ring(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.create_ring(data["ring_title"])

    # @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_create_pools(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.create_pools(data["pools_number"])

    # @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_add_participants_to_pool(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.add_participants_to_pool()

    # @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_set_ring_for_pool(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.set_ring_for_pool()

    # @pytest.mark.skipif(data["type_id"] != 1, reason="Stage type is not pools")
    def test_user_can_delete_pools(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_pools(data["pools_number"])

    # @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_add_participants_to_swiss(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.add_participants_to_swiss()

    # @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_delete_swiss_rounds(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_swiss_rounds()

    # @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_set_ring_for_swiss_round(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.set_ring_for_pairs()

    # @pytest.mark.skipif(data["type_id"] != 3 and data["type_id"] != 4, reason="Stage type is not swiss system")
    def test_user_can_set_pairs_for_swiss_round(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.change_pairs()

    def test_user_can_create_playoff_stage(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.create_playoff(data["stage_fight_time"], data["finals_mode"], data["third_place"])

    def test_user_can_delete_playoffs(self, browser, data):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_playoff_stages(data["go_next_stage"])

    def test_user_can_delete_pools_stage(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_pools_stage()

    def test_user_can_delete_playoff_stage(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_playoff()

    def test_user_can_delete_nomination(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_nomination()

    def test_user_can_delete_ring(self, browser):
        """start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament(data["title"])"""
        page = TournamentPage(browser, browser.current_url)
        page.delete_ring()

    def test_user_can_open_registration(self, browser):
        page = TournamentPage(browser, browser.current_url)
        page.enable_hemagon_reg()
        page.change_tournament_status(3)

    def test_user_can_register_for_the_tournament(self, browser):
        page = TournamentPage(browser, browser.current_url)
        page.register_for_the_tournament()

    def test_user_can_change_application(self, browser):
        page = TournamentPage(browser, browser.current_url)
        page.change_application()

    def test_user_can_handle_participants(self, browser):
        page = TournamentPage(browser, browser.current_url)
        page.handle_participants()
