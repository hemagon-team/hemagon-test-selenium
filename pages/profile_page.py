from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    def should_be_profile_page(self):
        self.should_be_profile_url()
        self.should_be_summary_tab()

    def should_be_profile_url(self):
        assert "users" in self.browser.current_url, "No 'users' in page URL"

    def should_be_summary_tab(self):
        assert self.is_element_present(ProfilePageLocators.SUMMARY_TAB)

    def should_be_user_name(self):
        assert self.is_element_present(ProfilePageLocators.USER_NAME)

    def should_be_user_club(self):
        assert self.is_element_present(ProfilePageLocators.USER_CLUB)
