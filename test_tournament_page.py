import os
import time
import pytest
from datetime import date
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.organizer_page import OrganizerPage

base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

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

type_id = 1             # Possible values: 1 (pools) / 2 (playoff) / 3 (swiss system) / 4 (swiss system with hits)
to_the_finals = False
stage_fight_time = 120

go_next_stage = 8
playoff_size = 8        # Possible values: 4 / 8 / 16 / 32 / 64
finals_mode = 1         # Possible values: 1 (best of 1) or 2 (best of 3)
swiss_empty_win = True  # Possible values: True (win) or False (draw)
hits_initial_hp = 10
hits_limit_hp = 0

participants_number = 8

ring_title = "Ring" + str(time.time())

pools_number = (participants_number + 7 - 1) // 7


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.login_user(test_email, test_password)
    page.should_be_authorized_user()
    # Close cookies
    page.close_cookies()


class TestUserCanModifyTournament:
    # Not the best way to organize setup
    # THINK OF A BETTER LOGIC
    def test_setup_create_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.create_tournament(title, start_date, end_date, country, city, description)

    def test_user_can_create_nomination(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.create_nomination(nomination_title, weapon_id, fight_time, last_round_time)

    def test_user_can_create_stage(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.create_stage(type_id, to_the_finals, fight_time, go_next_stage, )

    def test_user_can_add_participants(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.add_participants(str(participants_number))

    def test_user_can_create_ring(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.create_ring(ring_title)

    def test_user_can_create_pools(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.create_pools(pools_number)

    def test_user_can_add_participants_to_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.add_participants_to_pool()

    def test_user_can_set_ring_for_pool(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.set_ring_for_pool()

    def test_user_can_delete_pools(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.delete_pools(pools_number)

    def test_user_can_delete_stage(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.delete_stage()

    def test_user_can_delete_nomination(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.delete_nomination()

    def test_user_can_delete_ring(self, browser):
        start_page = OrganizerPage(browser, link)
        start_page.open()
        start_page.open_tournament()
        page = TournamentPage(browser, browser.current_url)
        page.delete_ring()

    # Not the best way to organize teardown
    # THINK OF A BETTER LOGIC
    def test_teardown_delete_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.delete_tournament()
