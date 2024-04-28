from .base_page import BasePage
from .locators import MainPageLocators
import time


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

    """def open_fighters_tab(self):
        self.click_button(MainPageLocators.FIGHTERS_TAB)
        assert self.is_element_present(MainPageLocators.FIGHTERS_TITLE)

    def open_clubs_tab(self):
        self.click_button(MainPageLocators.CLUBS_TAB)
        assert self.is_element_present(MainPageLocators.CLUBS_TITLE)"""

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

    def open_rating_for_every_weapon(self):
        self.open_rating_tab()
        weapon_tabs = self.find_multiple_elements_wait(MainPageLocators.RATING_WEAPON_TABS)
        for tab in weapon_tabs:
            weapon_tab_name = tab.text
            weapon_tab_name = " ".join(weapon_tab_name.split(" ")[:-1]).lower()
            tab.click()
            weapon_title = self.find_element_wait(MainPageLocators.RATING_WEAPON_TITLE)
            weapon_title_name = weapon_title.text
            weapon_title_name = weapon_title_name.lower()
            assert weapon_tab_name in weapon_title_name, ("Incorrect title: should "
                                                          f"contain {weapon_tab_name}, is {weapon_title_name}")

    def open_rating_overall_list_for_every_weapon(self):
        self.open_rating_tab()
        weapon_tabs = self.find_multiple_elements_wait(MainPageLocators.RATING_WEAPON_TABS)
        tabs_number = len(weapon_tabs)
        for i in range(tabs_number):
            weapon_tabs = self.find_multiple_elements_wait(MainPageLocators.RATING_WEAPON_TABS)
            tab = weapon_tabs[i]
            weapon_tab_text = tab.text
            weapon_tab_name = " ".join(weapon_tab_text.split(" ")[:-1]).lower()
            noms_number = int(weapon_tab_text[-1])
            tab.click()
            if noms_number == 1:
                self.click_button(MainPageLocators.RATING_OPEN_LIST_BUTTON)
            else:
                self.click_button(MainPageLocators.RATING_OPEN_LIST_OVERALL_BUTTON)
            self.wait_for_element(MainPageLocators.RATING_LIST_INPUT)
            nom_title = self.find_element_wait(MainPageLocators.RATING_LIST_TITLE)
            nom_title_name = nom_title.text
            nom_title_name = nom_title_name.lower()
            assert weapon_tab_name in nom_title_name, (f"Incorrect title: should contain {weapon_tab_name}, "
                                                       f"is {nom_title_name}")
            assert self.is_element_present(MainPageLocators.RATING_LIST_TABLE), "No table"
            self.browser.back()
            i += 1

    def open_rating_about(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_ABOUT_LINK)
        assert self.is_element_present(MainPageLocators.RATING_ABOUT_TITLE)

    def open_rating_import(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_IMPORT_LINK)
        assert self.is_element_present(MainPageLocators.RATING_IMPORT_TITLE)
