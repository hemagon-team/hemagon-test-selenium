from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        # Think of a way to assert main page
        pass

    def open_tournaments_tab(self):
        self.click_button(MainPageLocators.TOURNAMENTS_TAB)
        assert self.is_element_present(MainPageLocators.TOURNAMENT_STATUS_TITLE)

    def open_rating_tab(self):
        self.click_button(MainPageLocators.RATING_TAB)
        assert self.is_element_present(MainPageLocators.RATING_TITLE)

    def open_fighters_tab(self):
        self.click_button(MainPageLocators.FIGHTERS_TAB)
        assert self.is_element_present(MainPageLocators.FIGHTERS_TITLE)

    def open_clubs_tab(self):
        self.click_button(MainPageLocators.CLUBS_TAB)
        assert self.is_element_present(MainPageLocators.CLUBS_TITLE)

    def open_achievements_tab(self):
        self.click_button(MainPageLocators.ACHIEVEMENTS_TAB)
        assert self.is_element_present(MainPageLocators.ACHIEVEMENTS_TITLE)

    def open_about_tab(self):
        # For some reason doesn't work
        # FIX NEEDED
        self.click_button(MainPageLocators.ABOUT_TAB)
        assert self.is_element_present(MainPageLocators.ABOUT_TITLE)

    def open_contact_tab(self):
        self.click_button(MainPageLocators.CONTACT_TAB)
        assert self.is_element_present(MainPageLocators.CONTACT_TITLE)
