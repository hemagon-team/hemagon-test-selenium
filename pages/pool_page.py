import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import StagePageLocators
from .locators import FightPageLocators
from .locators import PoolPageLocators
from .fight_page import FightPage

class PoolPage(BasePage):

    def run_pool(self):
        x = 3
        numberoffights = self.find_multiple_elements_wait(PoolPageLocators.FIGHT_ROW)
        numberoffights = (len(numberoffights) + x)
        while x < numberoffights:
            x += 1
            if x == numberoffights:
                currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(3) > div:nth-child(1)'
                fightbutton = self.browser.find_element(By.CSS_SELECTOR, currentfight)
                fightbutton.click()
                time.sleep(3)
                FightPage.fight(self)
                self.click_button(PoolPage.CLOSE_POOL_BUTTON)
                break
        currentfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(3) > div:nth-child(1)'
        self.click_button(PoolPage.CLOSE_POOL_BUTTON)
        time.sleep(3)
        FightPage.fight(self)
