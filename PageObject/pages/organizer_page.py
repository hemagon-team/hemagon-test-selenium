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
        create_tournament_button = self.browser.find_element(*OrganizerPageLocators.CREATE_TOURNAMENT_BUTTON)
        create_tournament_button.click()
        # Choose test tournament option: yes
        test_tournament_input = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(OrganizerPageLocators.TEST_TOURNAMENT_INPUT)
        )
        test_tournament_input.click()
        # Enter a title of the tournament
        title_field = self.browser.find_element(*OrganizerPageLocators.TITLE_FIELD)
        title_field.send_keys(title)
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
        description_field = self.browser.find_element(*OrganizerPageLocators.DESCRIPTION_FIELD)
        description_field.send_keys(description)
        # Save the tournament
        save_button = self.browser.find_element(*OrganizerPageLocators.SAVE_BUTTON)
        save_button.click()

    def open_tournament(self):
        tournament_banner = self.browser.find_element(*OrganizerPageLocators.TOURNAMENT_BANNER)
        tournament_banner.click()
