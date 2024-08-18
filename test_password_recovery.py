import os
import json
import pytest
from pages.login_page import LoginPage
from pages.password_page import PasswordPage
from pages.tournament_page import TournamentPage
from pages.main_page import MainPage
from pages.stages_page import StagesPage
from pages.organizer_page import OrganizerPage
from pages.locators import TournamentPageLocators
from pages.locators import PostalPageLocators
import time


# Set links
base_link = os.environ["TEST_BASEURL"]
link = base_link + '/login'
post_link = os.environ["TEST_POSTAL_LINK"]

# Set User
current_email = os.environ["TEST_USER_EMAIL"]
current_password = os.environ["TEST_USER_PASSWORD"]
postal_password = os.environ["TEST_POSTAL_PASSWORD"]

# Set user data (modify in data.json)
with open("data.json", "r") as f:
    data = json.load(f)

@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.go_to_login_page()
    # Close cookies
    page.close_cookies()
    #time.sleep(3)

class TestPasswordRecovery:
    
    def test_user_can_recover_the_password(self, browser):
        
        page = PasswordPage(browser, link)
        page.open()

        page.ask_password_recovery_code(current_email)
        the_code = page.get_recovery_code(post_link, current_email, postal_password)
        time.sleep(2)
        page.set_new_password(the_code)

        time.sleep(3)
