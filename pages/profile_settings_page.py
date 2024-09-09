import time
import json
#from selenium.webdriver.common.by import By
from .base_page import BasePage
#from .locators import LoginPageLocators
from .locators import RegistrationPageLocators
from .locators import ProfileSettingsLocators
#from .locators import OrganizerPageLocators
from selenium.webdriver.common.keys import Keys

# Set user data (modify in data.json)
with open("/home/thatsme/git/hemagon-test-selenium/data/other/user_data.json", "r") as f:
    data = json.load(f)

class ProfileSettingsPage(BasePage):

    def open_settings(self):
        self.click_button(RegistrationPageLocators.PROFILE_BUTTON)
        self.click_button(RegistrationPageLocators.SETTINGS_BUTTON)

    def user_can_change_the_name(self):
        field = self.find_element_wait(ProfileSettingsLocators.FIRST_NAME_FIELD)
        field.send_keys(Keys.CONTROL + 'a')
        field.send_keys(Keys.BACKSPACE)
        self.fill_input(ProfileSettingsLocators.FIRST_NAME_FIELD, data['first_name1'])
        time.sleep(1)
        self.click_button(ProfileSettingsLocators.SAVE_BUTTON)
        prof_btn = self.find_element_wait(RegistrationPageLocators.PROFILE_BUTTON)
        firstname = data['first_name1']
        assert firstname in prof_btn.text
    
    def user_can_change_the_last_name(self):
        field = self.find_element_wait(ProfileSettingsLocators.LAST_NAME_FIELD)
        field.send_keys(Keys.CONTROL + 'a')
        field.send_keys(Keys.BACKSPACE)
        self.fill_input(ProfileSettingsLocators.LAST_NAME_FIELD, data['last_name1'])
        time.sleep(1)
        self.click_button(ProfileSettingsLocators.SAVE_BUTTON)
        prof_btn = self.find_element_wait(RegistrationPageLocators.PROFILE_BUTTON)
        lastname = data['last_name1']
        assert lastname in prof_btn.text
        
    def user_can_change_the_country(self):
        country = self.find_element_wait(ProfileSettingsLocators.COUNTRY_FIELD)
        #self.click_button(ProfileSettingsLocators.CLEAR_COUNTRY_BUTTON)
        country.send_keys(Keys.BACKSPACE)
        country.send_keys(data["country1"])
        time.sleep(2)
        country.send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_button(ProfileSettingsLocators.SAVE_BUTTON)
    
    def user_can_change_the_city(self):
        city = self.find_element_wait(ProfileSettingsLocators.CITY_FIELD)
        #self.click_button(ProfileSettingsLocators.CLEAR_CITY_BUTTON)
        city.send_keys(Keys.BACKSPACE)
        city.send_keys(data["city1"])
        time.sleep(2)
        city.send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_button(ProfileSettingsLocators.SAVE_BUTTON)

    def user_can_change_the_email(self):
        field = self.find_element_wait(ProfileSettingsLocators.EMAIL_FIELD)
        field.send_keys(Keys.CONTROL + 'a')
        field.send_keys(Keys.BACKSPACE)
        self.fill_input(ProfileSettingsLocators.EMAIL_FIELD, data["email1"])

