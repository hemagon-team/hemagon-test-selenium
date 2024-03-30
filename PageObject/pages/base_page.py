import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_BUTTON), "Login link is not present"

    def go_to_login_page(self):
        login_button = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        login_button.click()

    def go_to_organizer_page(self):
        user_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(BasePageLocators.USER_NAME)
        )
        user_name.click()
        my_tournaments_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(BasePageLocators.MY_TOURNAMENTS_BUTTON)
        )
        my_tournaments_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_NAME), "User is not authorized"
