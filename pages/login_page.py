from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No 'login' in page URL"

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.EMAIL_FIELD), "Email field is not presented"

    def login_user(self, email, password):
        self.fill_input(LoginPageLocators.EMAIL_FIELD, email)
        self.fill_input(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_button(LoginPageLocators.LOGIN_BUTTON)
