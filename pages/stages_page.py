import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import StagePageLocators
from .pool_page import PoolPage
from selenium.webdriver.common.by import By
import random
from random import randint

class StagesPage(BasePage):
    bro = webdriver.Chrome()
    bro.implicitly_wait(15) 
    def pools_running(self):

        allpools = self.find_multiple_elements_wait(StagePageLocators.POOLS_NUMBER)
        numberofpools = len(allpools)

# имеет смысл While переписать на for
        pool = 0
        while True:
            if pool == numberofpools:
                break
            buttonlocator = 'btn-stage-0-pool-' + str(pool) +'-run'
            runbutton = StagesPage.bro.find_elements(By.ID, buttonlocator)
            runbutton.click()
            time.sleep(1)
            

            poolpage = PoolPage(self)
            poolpage.run_pool(self)
            pool += 1
    
    def playoff_create(self):
        self.click_button(StagePageLocators.NEXT_STAGE_BUTTON)
  
    def branch_running(self, sidechoise):
        rounds = 1
        while True: 
            roundsnumber = StagesPage.bro.find_elements(By.ID, sidechoise)
            roundsnumber = len(roundsnumber)
            if rounds != roundsnumber:
                roundlocator = 'div.rounds-container.eliminations > div:nth-child(' + str(rounds) + ')> div:nth-child(2) > div:nth-child(1)'
                round_run = roundlocator + ' > a > button' 

                runbranch = StagesPage.find_element_wait(By.CSS_SELECTOR, round_run)
                runbranch.click()
                PoolPage.run_pool(self)
                break
            else:
                roundlocator = 'div.rounds-container.eliminations > div:nth-child(' + str(rounds) + ')> div:nth-child(2) > div:nth-child(1)'
                round_run = roundlocator + ' > a > button' 
                runbranch = StagesPage.find_element_wait(By.CSS_SELECTOR, round_run)
                runbranch.click()
                PoolPage.run_pool(self)
                roundbuild = roundlocator + ' > #btn-stage-1-side-0-build-next-playoff-round:last-of-type'
                roundbuildbutton = StagesPage.find_element_wait(By.CSS_SELECTOR, roundbuild)
                roundbuildbutton.click()
                rounds += 1
                time.sleep(1)

    def branches_order(self):
        choose_branch = randint(0, 1)
        if choose_branch == 0:
            self.branch_running(self, StagePageLocators.LEFT_BRANCH_RUN_BUTTON) #должно быть self, не StagesPage
            self.branch_running(self, StagePageLocators.RIGHT_BRANCH_RUN_BUTTON)

        else:
            self.branch_running(self, StagePageLocators.RIGHT_BRANCH_RUN_BUTTON)
            self.branch_running(self, StagePageLocators.LEFT_BRANCH_RUN_BUTTON)
        self.click_button(StagePageLocators.NEXT_PLAYOFF_STAGE_BUTTON)

        
    def finals_running(self):
        allfinalbuttons = StagesPage.bro.find_elements(StagePageLocators.FINALS_RUN_BUTTON)
        finalsrunbuttonposition = len(allfinalbuttons)
        finalsrunbuttonselector = 'div.rounds-container.eliminations > div:nth-child(' + str(finalsrunbuttonposition) + ') > div:nth-child(2) > div:nth-child(1) > a > #btn-stage-1-side-0-run-playoff-round'
        finalsrunbutton = StagesPage.find_element_wait(By.CSS_SELECTOR, finalsrunbuttonselector)
        finalsrunbutton.click()
        PoolPage.run_pool(self)
    
    def playoff_running(self):
        self.branches_order(self)
        time.sleep(1)
        self.finals_running(self)