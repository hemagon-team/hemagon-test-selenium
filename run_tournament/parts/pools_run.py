from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from parts.login import login
from parts.run_pool import run_pool




def pools_run(self):

    login(self)

    pool_num = self.browser.find_elements(By.CSS_SELECTOR, 'div.pool')
    pool_num = len(pool_num)
    pl = 0
    #while pl < pool_num:
    while True:
        if pl == pool_num:
            break
        loc_run = 'btn-stage-0-pool-' + str(pl) +'-run'
        pool_run = self.browser.find_element(By.ID, loc_run)
        pool_run.click()
        time.sleep(1)
            
        run_pool(self)
        pl += 1
        