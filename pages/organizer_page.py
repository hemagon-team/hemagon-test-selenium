import time
from .base_page import BasePage
from .locators import OrganizerPageLocators


class OrganizerPage(BasePage):

    def should_be_organizer_url(self):
        assert "organizer" in self.browser.current_url, "No 'organizer' in page URL"
        time.sleep(0.2)

    def create_tournament(self, title, url, start_date, end_date, country, city, description):
        # Create a new tournament
        self.click_button(OrganizerPageLocators.CREATE_TOURNAMENT_BUTTON)

        # Choose test tournament option: yes
        self.click_button(OrganizerPageLocators.TEST_TOURNAMENT_INPUT)

        # Enter a title of the tournament
        self.fill_input(OrganizerPageLocators.TITLE_FIELD, title)

        # Enter URL of the tournament
        self.fill_input(OrganizerPageLocators.URL_FIELD, url)

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
        self.fill_search_input(OrganizerPageLocators.COUNTRY_FIELD, country)

        # Choose a city
        self.fill_search_input(OrganizerPageLocators.CITY_FIELD, city)

        # Add description
        self.fill_input(OrganizerPageLocators.DESCRIPTION_FIELD, description)

        # Save the tournament
        self.click_button(OrganizerPageLocators.SAVE_BUTTON)

        # Wait so that name check don't handle creating page title
        time.sleep(0.3)

    def open_tournament(self, title):
        banners = self.find_multiple_elements_wait(OrganizerPageLocators.TOURNAMENT_BANNERS)
        for banner in banners:
            if banner.text == title:
                banner.click()
                break
        self.wait_for_element(OrganizerPageLocators.TOURNAMENT_OVERVIEW_TAB)

    def delete_tournament(self, title):
        self.open_tournament(title)
        self.click_button(OrganizerPageLocators.REMOVE_TOURNAMENT_BUTTON)
        self.confirm_alert()
