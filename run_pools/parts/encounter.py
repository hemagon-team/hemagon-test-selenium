from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint


def encounter(self):
    html = self.browser.find_element(By.TAG_NAME, 'html')
    rd_plus_points = self.browser.find_element(By.CSS_SELECTOR, 'div.scores-buttons-left > div:nth-child(1) > button')
    bl_plus_points = self.browser.find_element(By.CSS_SELECTOR, 'div.scores-buttons-right > div:nth-child(1) > button')
            
    timerrand = random.randint(2, 7)

    siderand = randint(0, 1)
    scorerand = randint(1, 2)
    html.send_keys(Keys.SPACE)
    time.sleep(timerrand)
    html.send_keys(Keys.SPACE)
    i = 0
    if siderand == 0:
        while i < scorerand:
            rd_plus_points.click()
            i += 1
    else:
        while i < scorerand:
            bl_plus_points.click()
            i += 1
    time.sleep(1)