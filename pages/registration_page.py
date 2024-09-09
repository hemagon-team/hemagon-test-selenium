import time
import json
#from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationPageLocators
from .locators import OrganizerPageLocators
from selenium.webdriver.common.keys import Keys

# Set user data (modify in data.json)
with open("/home/thatsme/git/hemagon-test-selenium/data/other/user_data.json", "r") as f:
    data = json.load(f)

test_organizer = data['trial']
if test_organizer == "yes":
    test_organizer = True
else:
    test_organizer = False

class RegistrationPage(BasePage):

    def user_can_open_the_registration_form(self):
        self.click_button(LoginPageLocators.ACCOUNT_REGISTRATION)
        # rrr = self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Register a new account')
        # rrr.click()
    
    def user_can_fill_the_form(self):
        self.fill_input(RegistrationPageLocators.FIRST_NAME, data["first_name"])
        self.fill_input(RegistrationPageLocators.LAST_NAME, data["last_name"])
        self.fill_input(RegistrationPageLocators.EMAIL, data["email"])
        self.fill_input(RegistrationPageLocators.PASSWORD, data["password"])
        self.fill_input(RegistrationPageLocators.PASSWORD_CONFIRMATION, data["password"])
        
        if test_organizer:
            self.click_button(RegistrationPageLocators.ORGANIZER_YES)
        else:
            self.click_button(RegistrationPageLocators.ORGANIZER_NO)
        
        self.click_button(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        time.sleep(3)

    def user_can_update_the_profile(self):
        if test_organizer:
            self.click_button(RegistrationPageLocators.PROFILE_BUTTON)
            self.click_button(RegistrationPageLocators.SETTINGS_BUTTON)
        country = self.find_element_wait(OrganizerPageLocators.COUNTRY_FIELD)
        city = self.find_element_wait(OrganizerPageLocators.CITY_FIELD)
        country.send_keys(data["country"])
        time.sleep(2)
        country.send_keys(Keys.ENTER)
        time.sleep(1)
        city.send_keys(data["city"])
        time.sleep(2)
        city.send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_button(RegistrationPageLocators.SAVE_BUTTON)

    def user_can_log_out(self):
        self.click_button(RegistrationPageLocators.PROFILE_BUTTON)
        self.click_button(RegistrationPageLocators.LOG_OUT_BUTTON)
    
    def user_can_log_in(self, email, password):
        self.fill_input(LoginPageLocators.EMAIL_FIELD, email)
        self.fill_input(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_button(LoginPageLocators.LOGIN_BUTTON)
        
        prof_btn = self.find_element_wait(RegistrationPageLocators.PROFILE_BUTTON)
        full_name = data['first_name'] + ' ' + data['last_name']
        assert full_name in prof_btn.text

        time.sleep(4)
