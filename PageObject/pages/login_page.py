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
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "Email field is not presented"

    def login_user(self, email, password):
        email_field = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD)
        )
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
