import time
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
  
    def pools_running(self):
        numberofpools = self.find_elements(StagePageLocators.POOLS_NUMBER)
        numberofpools = len(numberofpools)

        pool = 0
        while True:
            if pool == numberofpools:
                break
            buttonlocator = 'btn-stage-0-pool-' + str(pool) +'-run'
            runbutton = self.browser.find_element(By.ID, buttonlocator)
            runbutton.click()
            time.sleep(1)
            
            PoolPage.run_pool(self)
            pool += 1
    
    def playoff_create(self):
        self.click_button(StagePageLocators.NEXT_STAGE_BUTTON)
  
    def branch_running(self, sidechoise):
        rounds = 1
        while True: 
            roundsnumber = self.browser.find_elements(By.ID, sidechoise)
            roundsnumber = len(roundsnumber)
            if rounds != roundsnumber:
                roundlocator = 'div.rounds-container.eliminations > div:nth-child(' + str(rounds) + ')> div:nth-child(2) > div:nth-child(1)'
                round_run = roundlocator + ' > a > button' 

                runbranch = self.browser.find_element(By.CSS_SELECTOR, round_run)
                runbranch.click()
                PoolPage.run_pool(self)
                break
            else:
                roundlocator = 'div.rounds-container.eliminations > div:nth-child(' + str(rounds) + ')> div:nth-child(2) > div:nth-child(1)'
                round_run = roundlocator + ' > a > button' 
                runbranch = self.browser.find_element(By.CSS_SELECTOR, round_run)
                runbranch.click()
                PoolPage.run_pool(self)
                roundbuild = roundlocator + ' > #btn-stage-1-side-0-build-next-playoff-round:last-of-type'
                roundbuildbutton = self.browser.find_element(By.CSS_SELECTOR, roundbuild)
                roundbuildbutton.click()
                rounds += 1
                time.sleep(1)

    def branches_order(self):
        choose_branch = randint(0, 1)
        if choose_branch == 0:
            StagesPage.branch_running(self, StagePageLocators.LEFT_BRANCH_RUN_BUTTON)
            StagesPage.branch_running(self, StagePageLocators.RIGHT_BRANCH_RUN_BUTTON)

        else:
            StagesPage.branch_running(self, StagePageLocators.RIGHT_BRANCH_RUN_BUTTON)
            StagesPage.branch_running(self, StagePageLocators.LEFT_BRANCH_RUN_BUTTON)
        self.click_button(StagePageLocators.NEXT_PLAYOFF_STAGE_BUTTON)

    def finals_running(self):
        finalsrunbutton = self.find_multiple_elements_wait(StagePageLocators.FINALS_RUN_BUTTON)
        finalsrunbutton = len(finalsrunbutton)
        finalsrunbutton = 'div.rounds-container.eliminations > div:nth-child(' + str(finalsrunbutton) + ') > div:nth-child(2) > div:nth-child(1) > a > #btn-stage-1-side-0-run-playoff-round'
        finalsrunbutton = self.find_element_wait(By.CSS_SELECTOR, finalsrunbutton)
        finalsrunbutton.click()
        PoolPage.run_pool(self)
    
    def playoff_running(self):
        StagesPage.branches_order(self)
        time.sleep(1)
        StagesPage.finals_running(self)