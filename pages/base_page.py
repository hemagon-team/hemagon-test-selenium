import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_element_wait(self, selector):
        return WebDriverWait(self.browser, 5, poll_frequency=0.5).until(
            EC.presence_of_element_located(selector)
        )

    def is_element_present(self, selector):
        try:
            self.find_element_wait(selector)
        except NoSuchElementException:
            return False
        return True

    def fill_input(self, selector, value):
        input_field = self.find_element_wait(selector)
        input_field.clear()
        input_field.send_keys(value)

    def fill_select_by_text(self, selector, value):
        select_field = Select(self.find_element_wait(selector))
        select_field.select_by_visible_text(value)

    def fill_select_by_index(self, selector, index):
        select_field = Select(self.find_element_wait(selector))
        select_field.select_by_index(index)

    def click_button(self, selector):
        button = self.find_element_wait(selector)
        button.click()
        time.sleep(0.3)

    def wait_for_element(self, selector):
        WebDriverWait(self.browser, 5, poll_frequency=0.2).until(
            EC.presence_of_element_located(selector)
        )

    def confirm_alert(self):
        alert = WebDriverWait(self.browser, 5, poll_frequency=0.1).until(
            EC.alert_is_present()
        )
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_BUTTON), "Login link is not present"

    def go_to_login_page(self):
        self.click_button(BasePageLocators.LOGIN_BUTTON)

    def go_to_organizer_page(self):
        self.click_button(BasePageLocators.USER_NAME)
        self.click_button(BasePageLocators.MY_TOURNAMENTS_BUTTON)

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_NAME), "User is not authorized"

    def close_cookies(self):
        self.click_button(BasePageLocators.CLOSE_COOKIES_BUTTON)
