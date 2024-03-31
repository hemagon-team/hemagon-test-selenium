from pages.organizer_page import OrganizerPage
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
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


class TestUserCanCreateTournament:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(test_email, test_password)
        time.sleep(1)
        login_page.should_be_authorized_user()

    def test_user_can_create_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        time.sleep(1)
        page.create_tournament(title, start_date, end_date, country, city, description)

    def test_user_can_open_tournament(self, browser):
        page = OrganizerPage(browser, link)
        page.open()
        page.open_tournament()
        tournament_page = TournamentPage(browser, browser.current_url)
        time.sleep(1)
        tournament_page.should_be_tournament_title(title)
