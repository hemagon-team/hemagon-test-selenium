import os
import time
import pytest
from datetime import date
from pages.organizer_page import OrganizerPage
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage

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


class TestUserCanCreateTournament:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(test_email, test_password)
        login_page.should_be_authorized_user()

    def test_user_can_create_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.create_tournament(title, start_date, end_date, country, city, description)

    def test_user_can_open_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.open_tournament()
        tournament_page = TournamentPage(browser, browser.current_url)
        tournament_page.should_be_tournament_title(title)

    def test_user_can_delete_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.delete_tournament()
