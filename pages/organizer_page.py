from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import OrganizerPageLocators


class OrganizerPage(BasePage):

    def should_be_organizer_url(self):
        assert "organizer" in self.browser.current_url, "No 'organizer' in page URL"

    def create_tournament(self, title, start_date, end_date, country, city, description):
        # Create a new tournament
        self.click_button(OrganizerPageLocators.CREATE_TOURNAMENT_BUTTON)

        # Choose test tournament option: yes
        self.click_button(OrganizerPageLocators.TEST_TOURNAMENT_INPUT)

        # Enter a title of the tournament
        self.fill_input(OrganizerPageLocators.TITLE_FIELD, title)

        # FIX WORKING WITH DATE PICKERS
        '''
        # Set start date
        start_date_picker = self.browser.find_element(*OrganizerPageLocators.START_DATE_PICKER)
        start_date_picker.clear()
        start_date_picker.send_keys(start_date + Keys.ENTER)
        time.sleep(15)
        # Set end date
        end_date_picker = self.browser.find_element(*OrganizerPageLocators.END_DATE_PICKER)
        end_date_picker.send_keys(end_date)
        '''

        # Choose a country
        country_field = self.browser.find_element(*OrganizerPageLocators.COUNTRY_FIELD)
        country_field.send_keys(country + Keys.ENTER)
        time.sleep(2)
        country_field.send_keys(Keys.ENTER)

        # Choose a city
        city_field = self.browser.find_element(*OrganizerPageLocators.CITY_FIELD)
        city_field.send_keys(city + Keys.ENTER)
        time.sleep(2)
        city_field.send_keys(Keys.ENTER)

        # Add description
        self.fill_input(OrganizerPageLocators.DESCRIPTION_FIELD, description)

        # Save the tournament
        self.click_button(OrganizerPageLocators.SAVE_BUTTON)

    def open_tournament(self):
        self.click_button(OrganizerPageLocators.TOURNAMENT_BANNER)

    def delete_tournament(self):
        self.open_tournament()
        self.click_button(OrganizerPageLocators.REMOVE_TOURNAMENT_BUTTON)
        self.confirm_alert()
