import os
import pytest
from pages.organizer_page import OrganizerPage
from pages.login_page import LoginPage
from pages.tournament_page import TournamentPage
from datetime import date

# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + "/organizer/tournaments"

# Set User
email = os.environ["TEST_USER_EMAIL"]
password = os.environ["TEST_USER_PASSWORD"]

# Currently not runnable, can only be used as a part of test case


class TestUserCanCreateTournament:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_can_create_tournament(self, browser, data):
        page = OrganizerPage(browser, link)
        page.open()
        start_date = date.today().strftime("%d %B %Y")
        end_date = date.today().strftime("%d %B %Y")
        page.create_tournament(
            data["title"],
            start_date,
            end_date,
            data["country"],
            data["city"],
            data["description"]
        )

    def test_user_can_open_tournament(self, browser, data):
        """page = OrganizerPage(browser, link)
        page.open()
        page.open_tournament(data["title"])"""
        tournament_page = TournamentPage(browser, browser.current_url)
        tournament_page.should_be_tournament_title(data["title"])

    def test_user_can_delete_tournament(self, browser, data):
        page = OrganizerPage(browser, link)
        page.open()
        page.delete_tournament(data["title"])
