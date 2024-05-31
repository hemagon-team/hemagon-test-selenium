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
    def pools_running(self):

        allpools = self.find_multiple_elements_wait(StagePageLocators.POOLS_NUMBER)
        numberofpools = len(allpools)

# имеет смысл While переписать на for
        pool = 0
        while True:
            if pool == numberofpools:
                break
            buttonlocator = (By.ID, 'btn-stage-0-pool-' + str(pool) +'-run')
            runbutton = self.find_element_wait(buttonlocator)
            runbutton.click()
            time.sleep(1)
            

            #poolpage = PoolPage(url = any)
            PoolPage.run_pool(self)
            pool += 1
    
    def playoff_create(self):
        self.click_button(StagePageLocators.NEXT_STAGE_BUTTON)
  
    def left_branch_running(self):
        rounds = 1
        while True: 
            roundsnumber = self.find_multiple_elements_wait(StagePageLocators.LEFT_BRANCH_RUN_BUTTON)
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
                time.sleep(1)
                roundbuild = roundlocator + ' > #btn-stage-1-side-0-build-next-playoff-round:last-of-type'
                roundbuildbutton = self.browser.find_element(By.CSS_SELECTOR, roundbuild)
                roundbuildbutton.click()
                rounds += 1
                time.sleep(1)
    
    def right_branch_running(self):
        right_rounds = 1
        while True: 
            right_roundsnumber = self.find_multiple_elements_wait(StagePageLocators.RIGHT_BRANCH_RUN_BUTTON)
            right_roundsnumber = len(right_roundsnumber)
            if right_rounds != right_roundsnumber:
                right_roundlocator = 'div.rounds-container.eliminations > div:nth-child(' + str(right_rounds) + ')> div:nth-child(3) > div:nth-child(1)'
                right_round_run = right_roundlocator + ' > a > button' 

                right_runbranch = self.browser.find_element(By.CSS_SELECTOR, right_round_run)
                right_runbranch.click()
                PoolPage.run_pool(self)
                break
            else:
                right_roundlocator = 'div.rounds-container.eliminations > div:nth-child(' + str(right_rounds) + ')> div:nth-child(3) > div:nth-child(1)'
                right_round_run = right_roundlocator + ' > a > button' 
                right_runbranch = self.browser.find_element(By.CSS_SELECTOR, right_round_run)
                right_runbranch.click()
                PoolPage.run_pool(self)
                time.sleep(1)
                right_roundbuild = right_roundlocator + ' > #btn-stage-1-side-1-build-next-playoff-round:last-of-type'
                right_roundbuild = self.browser.find_element(By.CSS_SELECTOR, right_roundbuild)
                right_roundbuild.click()
                right_rounds += 1
                time.sleep(1)

    def branches_order(self):
        choose_branch = randint(0, 1)
        if choose_branch == 0:
            self.left_branch_running()
            self.right_branch_running()
            
        else:
            self.right_branch_running()
            self.left_branch_running()
        self.click_button(StagePageLocators.NEXT_PLAYOFF_STAGE_BUTTON)

        
    def finals_running(self):
        allfinalbuttons = self.find_multiple_elements_wait(StagePageLocators.FINALS_RUN_BUTTON)
        finalsrunbuttonposition = len(allfinalbuttons)
        finalsrunbuttonselector = 'div.rounds-container.eliminations > div:nth-child(' + str(finalsrunbuttonposition) + ') > div:nth-child(2) > div:nth-child(1) > a > #btn-stage-1-side-0-run-playoff-round'
        finalsrunbutton = self.browser.find_element(By.CSS_SELECTOR, finalsrunbuttonselector)
        finalsrunbutton.click()
        PoolPage.run_pool(self)
    
    def playoff_running(self):
        self.branches_order()
        time.sleep(1)
        self.finals_running()

    def swiss_running(self):
        roundsnumber = self.find_element_wait(StagePageLocators.RECOMMEND_SWISS_ROUNDS_NUMBER)
        roundsnumber = int(roundsnumber.text)
        x = 0
        while True:
            x += 1
            self.click_button(StagePageLocators.SWISS_RUN_POOL_BUTTON)
            PoolPage.run_swiss_pool(self)
            if x == roundsnumber:
                break
            self.click_button(StagePageLocators.BUILD_NEXT_SWISS_ROUND)
            time.sleep(4)
