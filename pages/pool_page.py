import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import PoolPageLocators
from .fight_page import FightPage
from selenium.common.exceptions import NoSuchElementException

class PoolPage(BasePage):

    def is_element(browser, by, value):
        try:
                element = browser.find_element(by, value)
                return True
        except NoSuchElementException:
            return False

    def run_pool(self):
        x = 0
        numberoffights = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_BUTTON)
        numberoffights = (len(numberoffights))

        fight_page = FightPage(self.browser, self.url)

        for x in range(0, numberoffights):
            fightbutton = self.browser.find_element(By.CSS_SELECTOR, 'button.small.active')
            fightbutton.click()            
            fight_page.fight()
            time.sleep(1)
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)

    def run_pool_with_random_results(self):
        self.click_button(PoolPageLocators.SEED_RANDOM_RESULTS_BUTTON)
        self.confirm_alert()
        self.wait_for_element_to_disappear(PoolPageLocators.RUN_FIGHT_BUTTON_ACTIVE)
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)

    def run_swiss_odd_pool(self):
        byebutton = self.find_element_wait(PoolPageLocators.BYE_BUTTON)
        byebutton.click()
        #the numeration of the fight selectors starts from 3 
        x = 3
        numberoffights = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_ROW)
        numberoffights = (len(numberoffights) + x)
        while x < numberoffights:
            x += 1
            if x == numberoffights:
                self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
                break
            currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(4) > div:nth-child(1) > button'
            fightbutton = self.browser.find_element(By.CSS_SELECTOR, currentfight)
            fightbutton.click()            
            FightPage.fight(self)
            time.sleep(1)

    def run_swiss_pool(self):
        #the numeration of the fight selectors starts from 3 
        x = 3
        numberoffights = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_ROW)
        numberoffights = (len(numberoffights) + x)
        while x < numberoffights:
            x += 1
            if x == numberoffights:
                currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(4) > div:nth-child(1) > button'
                fightbutton = self.browser.find_element(By.CSS_SELECTOR, currentfight)
                fightbutton.click()
                time.sleep(3)
                FightPage.fight(self)
                self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
                break
            currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(4) > div:nth-child(1) > button'
            fightbutton = self.browser.find_element(By.CSS_SELECTOR, currentfight)
            fightbutton.click()            
            FightPage.fight(self)
            time.sleep(1)

    def run_swiss(self):
        check_bye = self.is_element_present(PoolPageLocators.BYE_BUTTON)
        if not check_bye:
            PoolPage.run_swiss_pool(self)
        else:
            PoolPage.run_swiss_odd_pool(self)
