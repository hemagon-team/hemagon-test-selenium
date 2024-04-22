from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint
from parts.encounter import encounter
from parts.fight import fight

def run_pool(self):

    x = 3
    numfights = self.browser.find_elements(By.CSS_SELECTOR, 'div.pool > div.row')
    numfights = (len(numfights) + x)
    while x < numfights:
        x += 1
        close_btn = self.browser.find_element(By.CSS_SELECTOR, 'button.round')
        if x == numfights:
            locfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(3) > div:nth-child(1)'
            fight_btn = self.browser.find_element(By.CSS_SELECTOR, locfight)
            fight_btn.click()
            time.sleep(3)
            fight(self)
            close_btn.click()
            break
        locfight = 'div.pool > div:nth-child(' + str(x) + ') > div:nth-child(3) > div:nth-child(1)'
        fight_btn = self.browser.find_element(By.CSS_SELECTOR, locfight)
        fight_btn.click()
        time.sleep(3)
        fight(self)