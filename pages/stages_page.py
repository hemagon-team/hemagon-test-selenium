import time
from selenium.common.exceptions import ElementClickInterceptedException
from .base_page import BasePage
from .locators import StagePageLocators
from .pool_page import PoolPage
from selenium.webdriver.common.by import By
import random
from random import randint


class StagesPage(BasePage):
    def pools_running(self, full_mode=True):

        allpools = self.find_multiple_elements_wait(StagePageLocators.POOLS_NUMBER)
        numberofpools = len(allpools)

        # имеет смысл While переписать на for
        pool = 0
        while True:
            if pool == numberofpools:
                break
            buttonlocator = (By.ID, 'btn-stage-0-pool-' + str(pool) + '-run')
            runbutton = self.find_element_wait(buttonlocator)
            try:
                runbutton.click()
            except ElementClickInterceptedException:
                time.sleep(3)
                runbutton.click()
            time.sleep(1)

            pool_page = PoolPage(self.browser, self.url)
            if full_mode:
                pool_page.run_pool()
            else:
                pool_page.run_pool_with_random_results()
            pool += 1
    
    def playoff_create(self):
        self.click_button(StagePageLocators.NEXT_STAGE_BUTTON)
  
    def left_branch_running(self, full_mode=True):
        pool_page = PoolPage(self.browser, self.url)
        rounds = 1
        while True: 
            roundsnumber = self.find_multiple_elements_wait(StagePageLocators.LEFT_BRANCH_RUN_BUTTON)
            roundsnumber = len(roundsnumber)
            if rounds != roundsnumber:
                roundlocator = ('div.rounds-container.eliminations > div:nth-child(' + str(rounds) +
                                ')> div:nth-child(2) > div:nth-child(1)')
                round_run = roundlocator + '> div:nth-child(1) > a > button'

                runbranch = self.browser.find_element(By.CSS_SELECTOR, round_run)
                runbranch.click()
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
                break
            else:
                roundlocator = ('div.rounds-container.eliminations > div:nth-child(' + str(rounds) +
                                ')> div:nth-child(2) > div:nth-child(1)')
                round_run = roundlocator + '> div:nth-child(1) > a > button'
                runbranch = self.browser.find_element(By.CSS_SELECTOR, round_run)
                runbranch.click()
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
                time.sleep(1)
                roundbuild = roundlocator + ' > #btn-stage-1-side-0-build-next-playoff-round:last-of-type'
                roundbuildbutton = self.browser.find_element(By.CSS_SELECTOR, roundbuild)
                roundbuildbutton.click()
                rounds += 1
                time.sleep(1)
    
    def right_branch_running(self, full_mode=True):
        right_rounds = 1
        pool_page = PoolPage(self.browser, self.url)
        while True: 
            right_roundsnumber = self.find_multiple_elements_wait(StagePageLocators.RIGHT_BRANCH_RUN_BUTTON)
            right_roundsnumber = len(right_roundsnumber)
            if right_rounds != right_roundsnumber:
                right_roundlocator = ('div.rounds-container.eliminations > div:nth-child(' + str(right_rounds) +
                                      ')> div:nth-child(3) > div:nth-child(1)')
                right_round_run = right_roundlocator + '> div:nth-child(1) > a > button'

                right_runbranch = self.browser.find_element(By.CSS_SELECTOR, right_round_run)
                right_runbranch.click()
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
                break
            else:
                right_roundlocator = ('div.rounds-container.eliminations > div:nth-child(' + str(right_rounds) +
                                      ')> div:nth-child(3) > div:nth-child(1)')
                right_round_run = right_roundlocator + '> div:nth-child(1) > a > button'
                right_runbranch = self.browser.find_element(By.CSS_SELECTOR, right_round_run)
                right_runbranch.click()
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
                time.sleep(1)
                right_roundbuild = right_roundlocator + ' > #btn-stage-1-side-1-build-next-playoff-round:last-of-type'
                right_roundbuild = self.browser.find_element(By.CSS_SELECTOR, right_roundbuild)
                right_roundbuild.click()
                right_rounds += 1
                time.sleep(1)

    def branches_order(self, full_mode=True):
        choose_branch = randint(0, 1)
        if choose_branch == 0:
            self.left_branch_running(full_mode=full_mode)
            self.right_branch_running(full_mode=full_mode)
            
        else:
            self.right_branch_running(full_mode=full_mode)
            self.left_branch_running(full_mode=full_mode)
        self.click_button(StagePageLocators.NEXT_PLAYOFF_STAGE_BUTTON)

    def finals_running(self, full_mode=True):
        allfinalbuttons = self.find_multiple_elements_wait(StagePageLocators.FINALS_RUN_BUTTON)
        finalsrunbuttonposition = len(allfinalbuttons)
        finalsrunbuttonselector = ('div.rounds-container.eliminations > div:nth-child(' + str(finalsrunbuttonposition)
                                   + ') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a >'
                                     '#btn-stage-1-side-0-run-playoff-round')
        finalsrunbutton = self.browser.find_element(By.CSS_SELECTOR, finalsrunbuttonselector)
        finalsrunbutton.click()
        pool_page = PoolPage(self.browser, self.url)
        if full_mode:
            pool_page.run_pool()
        else:
            pool_page.run_pool_with_random_results()
    
    def playoff_running(self, full_mode=True):
        self.branches_order(full_mode=full_mode)
        time.sleep(1)
        self.finals_running(full_mode=full_mode)
