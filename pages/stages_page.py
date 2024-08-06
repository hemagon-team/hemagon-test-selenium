import time
from selenium.common.exceptions import ElementClickInterceptedException
from .base_page import BasePage
from .locators import StagePageLocators
from .pool_page import PoolPage
from .fight_page import FightPage
from .pool_page import PoolPageLocators
from .fight_page import FightPageLocators
from selenium.webdriver.common.by import By
import random
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class StagesPage(BasePage):

    def check_fight_pool_buttons(self):
        runbutton = self.browser.find_element(By.ID, 'btn-stage-0-pool-0-run')
        runbutton.click()
        time.sleep(1)
        fightbutton = self.browser.find_element(By.CSS_SELECTOR, 'div.pool > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > button')
        fightbutton.click()
        FightPage.button_checking(self)

    def check_fight_swiss_buttons(self):
        runbutton = self.browser.find_element(By.ID, 'btn-stage-0-pool-0-run')
        runbutton.click()
        time.sleep(1)
        fightbutton = self.browser.find_element(By.CSS_SELECTOR, 'div.pool > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > button')
        fightbutton.click()
        FightPage.swiss_button_checking(self)

    def pools_running(self, full_mode=True):
        allpools = self.find_multiple_elements_wait(StagePageLocators.POOLS_NUMBER)
        numberofpools = len(allpools)

        # имеет смысл While переписать на for
        pool = 0
        while True:
            if pool == numberofpools:
                break
            buttonlocator = StagePageLocators.POOL_START_BUTTON(pool)
            #runbutton = self.find_element_wait(buttonlocator)
            try:
                self.click_button(buttonlocator)
            except ElementClickInterceptedException:
                time.sleep(3)
                self.click_button(buttonlocator)
            time.sleep(1)

            pool_page = PoolPage(self.browser, self.url)
            if full_mode:
                pool_page.run_pool()
            else:
                pool_page.run_pool_with_random_results()
            pool += 1
    
    def playoff_create(self):
        self.click_button(StagePageLocators.NEXT_STAGE_BUTTON)
    
    def present_element(browser, by, value):
        try:
            element = browser.find_element(by, value)
            return True
        except NoSuchElementException:
            return False
  
    def left_branch_running(self, full_mode=True):
        pool_page = PoolPage(self.browser, self.url)
        rounds = 1
        while True:
            check_run = self.is_element_present(StagePageLocators.LEFT_RUN_BUTTON)
            if check_run:
                self.click_button(StagePageLocators.LEFT_RUN_BUTTON)
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
            else:
                check_build = self.is_element_present(StagePageLocators.LEFT_BRANCH_BUILD_BUTTON)
                if check_build:
                    rounds += 1
                    self.click_button(StagePageLocators.LEFT_BRANCH_BUILD_BUTTON)
                else:
                    break

    def right_branch_running(self, full_mode=True):
        pool_page = PoolPage(self.browser, self.url)
        rounds = 1
        while True:
            check_run = self.is_element_present(StagePageLocators.RIGHT_RUN_BUTTON)
            if check_run:
                self.click_button(StagePageLocators.RIGHT_RUN_BUTTON)
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
            else:
                check_build = self.is_element_present(StagePageLocators.RIGHT_BRANCH_BUILD_BUTTON)
                if check_build:
                    rounds += 1
                    self.click_button(StagePageLocators.RIGHT_BRANCH_BUILD_BUTTON)
                else:
                    break
    
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

    def swiss_running(self):
        html = self.find_element_wait(FightPageLocators.HTML)
        roundsnumber = self.find_element_wait(StagePageLocators.RECOMMEND_SWISS_ROUNDS_NUMBER)
        roundsnumber = int(roundsnumber.text)
        x = 0
        while True:
            self.click_button(StagePageLocators.SWISS_RUN_POOL_BUTTON)
            x += 1
            
            PoolPage.run_pool(self)
            if x == roundsnumber:
                break
            self.click_button(StagePageLocators.BUILD_NEXT_SWISS_ROUND)
            time.sleep(4)          

