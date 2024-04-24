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

    def open_rating_longsword(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_LONGSWORD)
        assert self.is_element_present(MainPageLocators.RATING_LONGSWORD_TITLE)

    def open_rating_saber(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_SABER)
        assert self.is_element_present(MainPageLocators.RATING_SABER_TITLE)

    def open_rating_rapier(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_RAPIER)
        assert self.is_element_present(MainPageLocators.RATING_RAPIER_TITLE)

    def open_rating_rapier_dagger(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_RAPIER_DAGGER)
        assert self.is_element_present(MainPageLocators.RATING_RAPIER_DAGGER_TITLE)

    def open_rating_dussak(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_DUSSAK)
        assert self.is_element_present(MainPageLocators.RATING_DUSSAK_TITLE)

    def open_rating_spear(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_SPEAR)
        assert self.is_element_present(MainPageLocators.RATING_SPEAR_TITLE)

    def open_rating_sword_buckler(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_SWORD_BUCKLER)
        assert self.is_element_present(MainPageLocators.RATING_SWORD_BUCKLER_TITLE)

    def open_rating_sidesword(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_SIDESWORD)
        assert self.is_element_present(MainPageLocators.RATING_SIDESWORD_TITLE)

    def open_rating_triathlon(self):
        self.open_rating_tab()
        self.click_button(MainPageLocators.RATING_TRIATHLON)
        assert self.is_element_present(MainPageLocators.RATING_TRIATHLON_TITLE)

    def open_rating_longsword_overall_list(self):
        self.open_rating_longsword()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_LONGSWORD_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_saber_overall_list(self):
        self.open_rating_saber()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_SABER_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_rapier_overall_list(self):
        self.open_rating_rapier()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_RAPIER_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_rapier_dagger_overall_list(self):
        self.open_rating_rapier_dagger()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_RAPIER_DAGGER_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_dussak_overall_list(self):
        self.open_rating_dussak()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_DUSSAK_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_spear_overall_list(self):
        self.open_rating_spear()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_SPEAR_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_sword_buckler_overall_list(self):
        self.open_rating_sword_buckler()
        self.click_button(MainPageLocators.RATING_OVERALL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_SWORD_BUCKLER_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_sidesword_overall_list(self):
        self.open_rating_sidesword()
        self.click_button(MainPageLocators.RATING_FULL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_SIDESWORD_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)

    def open_rating_triathlon_overall_list(self):
        self.open_rating_triathlon()
        self.click_button(MainPageLocators.RATING_FULL_BUTTON)
        assert self.is_element_present(MainPageLocators.RATING_TRIATHLON_OVERALL_TITLE)
        assert self.is_element_present(MainPageLocators.RATING_OVERALL_TABLE_USER)
