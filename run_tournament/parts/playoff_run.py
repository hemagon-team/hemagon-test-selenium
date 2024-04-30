from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
from parts.login import login
from random import randint
from parts.branches import branches
from parts.finals import finals

 
def playoff_run(self):

    #создали плейоф
    build_playoff_button = self.browser.find_element(By.ID, 'btn-stage-0-build-next-stage')
    build_playoff_button.click()
        
    #выбрали и запустили очерёдность веток
        
    branches(self)
    time.sleep(1)
    
    finals(self)
    time.sleep(3)
