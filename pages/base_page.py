import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_element_wait(self, selector):
        return WebDriverWait(self.browser, 5, poll_frequency=0.2).until(
            EC.presence_of_element_located(selector)
        )

    def find_multiple_elements_wait(self, selector):
        return WebDriverWait(self.browser, 5, poll_frequency=0.2).until(
            EC.presence_of_all_elements_located(selector)
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

    def fill_search_input(self, selector, value):
        search_field = self.find_element_wait(selector)
        search_field.send_keys(value + Keys.ENTER)
        time.sleep(2)
        search_field.send_keys(Keys.ENTER)

    def click_button(self, selector):
        button = WebDriverWait(self.browser, 5, poll_frequency=0.2).until(
            EC.element_to_be_clickable(selector)
        )
        button.click()
        time.sleep(0.3)

    def click_dropdown_element(self, trigger_selector, dropdown_selector, element_selector):
        trigger_element = self.find_element_wait(trigger_selector)
        ActionChains(self.browser).move_to_element(trigger_element).perform()
        dropdown_element = WebDriverWait(self.browser, 5, poll_frequency=0.3).until(
            EC.visibility_of_element_located(dropdown_selector)
        )
        element = dropdown_element.find_element(*element_selector)
        element.click()

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
        self.click_dropdown_element(BasePageLocators.USER_NAME, BasePageLocators.USER_POPOVER,
                                    BasePageLocators.MY_TOURNAMENTS_BUTTON)

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_NAME), "User is not authorized"

    def close_cookies(self):
        self.click_button(BasePageLocators.CLOSE_COOKIES_BUTTON)

    def open_contact_tab_from_footer(self):
        self.click_button(BasePageLocators.CONTACT_LINK_FOOTER)
        assert self.is_element_present(BasePageLocators.CONTACT_TITLE)

    def open_about_tab_from_footer(self):
        self.click_button(BasePageLocators.ABOUT_LINK_FOOTER)
        assert self.is_element_present(BasePageLocators.ABOUT_TITLE)
