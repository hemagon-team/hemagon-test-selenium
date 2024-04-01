from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.organizer_page import OrganizerPage
import time
from datetime import date
import pytest

base_link = "https://hemagon.com/"
link = "https://hemagon.com/organizer/tournaments"

test_email = "paulus.mair@mailfence.com"
test_password = "HEMAhuema@1"

title = "Test Tournament" + str(time.time())
start_date = date.today().strftime("%d %B %Y")
end_date = date.today().strftime("%d %B %Y")
country = "Spain"
city = "Barcelona"
description = "Test tournament"

nomination_title = "Nomination" + str(time.time())
weapon_id = 1
fight_time = "120"
last_round_time = "0"

type_id = 1
to_the_finals = False
stage_fight_time = 120
go_next_stage = 8
# playoff_size
# swiss_empty_win
# hits_initial_hp
# hits_limit_hp

participants_number = "16"

ring_title = "Ring" + str(time.time())


class TestUserCanModifyTournament:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = MainPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(test_email, test_password)
        time.sleep(1)
        page.should_be_authorized_user()
        # Close cookies
        page.close_cookies()

    # Not the best way to organize setup
    # THINK OF A BETTER LOGIC
    def test_setup_create_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.create_tournament(title, start_date, end_date, country, city, description)

    def test_user_can_create_nomination(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.create_nomination(nomination_title, weapon_id, fight_time, last_round_time)

    def test_user_can_create_stage(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.create_stage(type_id, to_the_finals, stage_fight_time, go_next_stage)

    def test_user_can_add_participants(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.add_participants(participants_number)

    def test_user_can_create_ring(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.create_ring(ring_title)

    def test_user_can_create_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.create_pool()
        # ADD FEATURE: CREATE ENOUGH POOLS FOR PARTICIPANTS NUMBER

    def test_user_can_add_participants_to_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.add_participants_to_pool()

    def test_user_can_set_ring_for_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.set_ring_for_pool()

    def test_user_can_delete_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.delete_pool()

    def test_user_can_delete_stage(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.delete_stage()

    def test_user_can_delete_nomination(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.delete_nomination()

    def test_user_can_delete_ring(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        time.sleep(1)
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        page.delete_ring()

    # Not the best way to organize teardown
    # THINK OF A BETTER LOGIC
    def test_teardown_delete_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.delete_tournament()
