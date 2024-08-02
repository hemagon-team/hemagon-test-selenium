import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import PoolPageLocators
from .fight_page import FightPage


class PoolPage(BasePage):

    def run_pool(self):
        fights_number = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_BUTTON)
        fights_number = (len(fights_number))

        fight_page = FightPage(self.browser, self.url)

        for x in range(0, fights_number):
            fight_button = self.browser.find_element(By.CSS_SELECTOR, 'div.row button.small.active')
            fight_button.click()
            fight_page.fight()
            time.sleep(0.3)
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)

    def run_pool_with_random_results(self):
        self.click_button(PoolPageLocators.SEED_RANDOM_RESULTS_BUTTON)
        self.confirm_alert()
        self.wait_for_element_to_disappear(PoolPageLocators.RUN_FIGHT_BUTTON_ACTIVE)
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)

    def run_swiss_pool(self, odd=False):
        # Check if there is a bye button, so the number of participants is odd
        if odd:
            bye_button = self.find_element_wait(PoolPageLocators.BYE_BUTTON)
            bye_button.click()

        # Determine number of fights in the pool
        x = 3  # the numeration of the fight selectors starts from 3
        fights_number = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_ROW)
        fights_number = (len(fights_number) + x)

        fight_page = FightPage(self.browser, self.url)

        # Run each fight
        while x < fights_number:
            x += 1
            if x == fights_number:
                # Run last fight in case it is not bye
                if not odd:
                    current_fight = ('div.pool > div:nth-child(' + str(x) +
                                     ') > div:nth-child(4) > div:nth-child(1) > button')
                    fight_button = self.browser.find_element(By.CSS_SELECTOR, current_fight)
                    fight_button.click()
                    time.sleep(0.3)
                    fight_page.fight()
                self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
                break
            # ???
            current_fight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(4) > div:nth-child(1) > button'
            fight_button = self.browser.find_element(By.CSS_SELECTOR, current_fight)
            fight_button.click()
            fight_page.fight()
            time.sleep(1)

    def run_swiss_pool_with_random_results(self):
        self.click_button(PoolPageLocators.SEED_RANDOM_RESULTS_BUTTON)
        self.confirm_alert()
        self.wait_for_element_to_disappear(PoolPageLocators.RUN_FIGHT_BUTTON_ACTIVE_SWISS)
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)

    def run_swiss(self, full_mode):
        if full_mode:
            check_bye = self.is_element_present(PoolPageLocators.BYE_BUTTON)
            self.run_swiss_pool(check_bye)
        else:
            self.run_swiss_pool_with_random_results()
