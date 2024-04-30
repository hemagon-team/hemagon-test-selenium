from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from parts.pools_run import pools_run
from parts.playoff_run import playoff_run

class Test_Pools_Run():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(15)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_pools_only(self):
        pools_run(self)
    
    time.sleep(1)

    def test_playoff_only(self):
        playoff_run(self)
    
    time.sleep(3)