import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import FightPageLocators
import random
from random import randint
from selenium.webdriver.common.by import By
from .locators import PoolPageLocators

class FightPage(BasePage):
    def encounter(self):
        html = self.find_element_wait(FightPageLocators.HTML)
           
        timerrand = random.randint(0, 0)

        sidechoise = randint(0, 1)
        scorerand = randint(1, 2)

        html.send_keys(Keys.SPACE)
        time.sleep(timerrand)
        html.send_keys(Keys.SPACE)

        i = 0
        if sidechoise == 0:
            while i < scorerand:
                self.click_button(FightPageLocators.ADD_LEFT_BUTTON)
                i += 1
        else:
            while i < scorerand:
                self.click_button(FightPageLocators.ADD_RIGHT_BUTTON)
                i += 1
        time.sleep(1)

    def button_checking(self):
        html = self.find_element_wait(FightPageLocators.HTML)
        html.send_keys(Keys.SPACE)
        html.send_keys(Keys.SPACE)       
        self.click_button(FightPageLocators.ADD_LEFT_BUTTON)
        self.click_button(FightPageLocators.MINUS_LEFT_BUTTON)
        self.click_button(FightPageLocators.ADD_RIGHT_BUTTON)
        self.click_button(FightPageLocators.MINUS_RIGHT_BUTTON)
        self.click_button(FightPageLocators.ADD_5SECONDS_BUTTON)
        self.click_button(FightPageLocators.TECHNICAL_DEFEAT_BUTTON)
        resetbutton = self.browser.find_element(By.CSS_SELECTOR, 'div.pool > div:nth-child(4) > div:nth-child(3) > div > button:nth-child(1)')
        resetbutton.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
        time.sleep(1)

    def swiss_button_checking(self):
        html = self.find_element_wait(FightPageLocators.HTML)
        html.send_keys(Keys.SPACE)
        html.send_keys(Keys.SPACE)       
        self.click_button(FightPageLocators.ADD_LEFT_BUTTON)
        self.click_button(FightPageLocators.MINUS_LEFT_BUTTON)
        self.click_button(FightPageLocators.ADD_RIGHT_BUTTON)
        self.click_button(FightPageLocators.MINUS_RIGHT_BUTTON)
        self.click_button(FightPageLocators.ADD_5SECONDS_BUTTON)
        self.click_button(FightPageLocators.TECHNICAL_DEFEAT_BUTTON)
        resetbutton = self.browser.find_element(By.CSS_SELECTOR, 'div.pool > div:nth-child(4) > div:nth-child(4) > div > button:nth-child(1)')
        resetbutton.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()
        self.click_button(PoolPageLocators.CLOSE_POOL_BUTTON)
        time.sleep(1)



    def fight(self):
        while True:
            redscore = self.find_element_wait(FightPageLocators.SCORE_LEFT)
            redscore = int(redscore.text)
            bluescore = self.find_element_wait(FightPageLocators.SCORE_RIGHT)
            bluescore = int(bluescore.text)

            if bluescore >= 2 or redscore >= 2:
                self.click_button(FightPageLocators.FINISH_BUTTON)
                break
            FightPage.encounter(self)
