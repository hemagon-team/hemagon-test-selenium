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

def fight(self):
    while True:
        redscore = self.browser.find_element(By.CSS_SELECTOR, 'div.sides > div:nth-child(1) > div.scores')
        redscore = int(redscore.text)
        bluescore = self.browser.find_element(By.CSS_SELECTOR, 'div.sides > div:nth-child(2) > div.scores')
        bluescore = int(bluescore.text)

        if bluescore >= 10 or redscore >= 10:
            finish_btn = self.browser.find_element(By.CSS_SELECTOR, 'div.bottom > button.btn.active')
            finish_btn.click()
            break
        encounter(self)