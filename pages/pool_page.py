import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import PoolPageLocators
from .fight_page import FightPage


class PoolPage(BasePage):

    def run_pool(self):
        # the numeration of the fight selectors starts from 3
        x = 3
        numberoffights = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_ROW)
        numberoffights = (len(numberoffights) + x)

        fight_page = FightPage(self.browser, self.url)

        while x < numberoffights:
            x += 1
            if x == numberoffights:
                currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(3) > div:nth-child(1)'
                fightbutton = self.browser.find_element(By.CSS_SELECTOR, currentfight)
                fightbutton.click()
                time.sleep(3)
                fight_page.fight()
                self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
                break

            currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(3) > div:nth-child(1)'
            fightbutton = self.browser.find_element(By.CSS_SELECTOR, currentfight)
            fightbutton.click()            
            # self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
            # x += 1
            # time.sleep(3)
            fight_page.fight()
            time.sleep(1)

    def run_pool_with_random_results(self):
        self.click_button(PoolPageLocators.SEED_RANDOM_RESULTS_BUTTON)
        self.confirm_alert()
        # self.wait_for_element(PoolPageLocators.SUCCESS_NOTIFICATION)
        time.sleep(5)
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
