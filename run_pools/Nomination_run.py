from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
from parts.login import login
from parts.run_pool import run_pool

class TestNomination_Run():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(15)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_nomination_run(self):

        login(self)

        pool_num = self.browser.find_elements(By.CSS_SELECTOR, 'div.pool')
        pool_num = len(pool_num)
        pl = 0
        while pl < pool_num:
            if pl == pool_num:
                break
            loc_run = 'btn-stage-0-pool-' + str(pl) +'-run'
            pool_run = self.browser.find_element(By.ID, loc_run)
            pool_run.click()
            time.sleep(1)
            run_pool(self)
            pl += 1
        time.sleep(3)