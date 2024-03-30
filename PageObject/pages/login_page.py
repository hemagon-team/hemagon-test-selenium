from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def login_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
