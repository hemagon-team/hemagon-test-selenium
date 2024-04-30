
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
from parts.run_pool import run_pool

def run_right(self): 
    rounds = 1

    while True: 
        rounds_num = self.browser.find_elements(By.ID, 'btn-stage-1-side-1-build-next-playoff-round')
        rounds_num = len(rounds_num)
        if rounds != rounds_num:
            loc_round = 'div.rounds-container.eliminations > div:nth-child(' + str(rounds) + ')> div:nth-child(3) > div:nth-child(1)'
            round_run = loc_round + ' > a > button' 

            run_br = self.browser.find_element(By.CSS_SELECTOR, round_run)
            run_br.click()
            run_pool(self)
            break
        else:
            loc_round = 'div.rounds-container.eliminations > div:nth-child(' + str(rounds) + ')> div:nth-child(3) > div:nth-child(1)'
            round_run = loc_round + ' > a > button' 

            run_br = self.browser.find_element(By.CSS_SELECTOR, round_run)
            run_br.click()
            run_pool(self)
            round_build = loc_round + ' > #btn-stage-1-side-1-build-next-playoff-round:last-of-type'
            round_build_btn = self.browser.find_element(By.CSS_SELECTOR, round_build)
            round_build_btn.click()

            rounds += 1
            time.sleep(1)
