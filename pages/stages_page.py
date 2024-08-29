import time
from .base_page import BasePage
from .locators import StagePageLocators
from .pool_page import PoolPage
from .fight_page import FightPage
from random import randint
from selenium.webdriver.common.by import By


class StagesPage(BasePage):

    def check_fight_pool_buttons(self):
        run_button = self.browser.find_element(By.ID, 'btn-stage-0-pool-0-run')
        run_button.click()
        time.sleep(1)
        fight_button = self.browser.find_element(By.CSS_SELECTOR, 'div.pool > div:nth-child(4) > div:nth-child(3) >'
                                                                  'div:nth-child(1) > button')
        fight_button.click()
        fight_page = FightPage(self.browser, self.url)
        fight_page.button_checking()

    def check_fight_swiss_buttons(self):
        run_button = self.browser.find_element(By.ID, 'btn-stage-0-pool-0-run')
        run_button.click()
        time.sleep(1)
        fight_button = self.browser.find_element(By.CSS_SELECTOR, 'div.pool > div:nth-child(4) > div:nth-child(4) >'
                                                                  'div:nth-child(1) > button')
        fight_button.click()
        fight_page = FightPage(self.browser, self.url)
        fight_page.swiss_button_checking()

    def pools_running(self, full_mode):
        # Determine number of pools
        pools_list = self.find_multiple_elements_wait(StagePageLocators.POOLS_NUMBER)
        pools_number = len(pools_list)

        # имеет смысл While переписать на for
        for pool in range(pools_number):
            button_locator = StagePageLocators.POOL_START_BUTTON(pool)
            self.click_button(button_locator)

            # Run pool (full or random)
            pool_page = PoolPage(self.browser, self.url)
            if full_mode:
                pool_page.run_pool()
            else:
                pool_page.run_pool_with_random_results()

    def playoff_create(self):
        self.click_button(StagePageLocators.NEXT_STAGE_BUTTON)

    def left_branch_running(self, full_mode):
        pool_page = PoolPage(self.browser, self.url)
        while True:
            check_run = self.is_element_present(StagePageLocators.LEFT_RUN_BUTTON)
            # Run stage (full or random) if there is an active run button
            if check_run:
                self.click_button(StagePageLocators.LEFT_RUN_BUTTON)
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
            else:
                check_build = self.is_element_present(StagePageLocators.LEFT_BRANCH_BUILD_BUTTON)
                # Build next stage if there is an active build next stage button
                if check_build:
                    self.click_button(StagePageLocators.LEFT_BRANCH_BUILD_BUTTON)
                else:
                    break

    def right_branch_running(self, full_mode):
        pool_page = PoolPage(self.browser, self.url)
        while True:
            check_run = self.is_element_present(StagePageLocators.RIGHT_RUN_BUTTON)
            # Run stage (full or random) if there is an active run button
            if check_run:
                self.click_button(StagePageLocators.RIGHT_RUN_BUTTON)
                if full_mode:
                    pool_page.run_pool()
                else:
                    pool_page.run_pool_with_random_results()
            else:
                check_build = self.is_element_present(StagePageLocators.RIGHT_BRANCH_BUILD_BUTTON)
                # Build next stage if there is an active build next stage button
                if check_build:
                    self.click_button(StagePageLocators.RIGHT_BRANCH_BUILD_BUTTON)
                else:
                    break

    def branches_order(self, full_mode):
        choose_branch = randint(0, 1)
        if choose_branch == 0:
            self.left_branch_running(full_mode)
            self.right_branch_running(full_mode)
        else:
            self.right_branch_running(full_mode)
            self.left_branch_running(full_mode)
        self.click_button(StagePageLocators.NEXT_PLAYOFF_STAGE_BUTTON)

    def finals_running(self, full_mode):
        # Define selector for finals run button
        finals_buttons_list = self.find_multiple_elements_wait(StagePageLocators.FINALS_RUN_BUTTON)
        finals_buttons_number = len(finals_buttons_list)
        finals_button_selector = ('div.rounds-container.eliminations > div:nth-child(' + str(finals_buttons_number)
                                  + ') > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a >'
                                    '#btn-stage-1-side-0-run-playoff-round')
        finals_run_button = self.browser.find_element(By.CSS_SELECTOR, finals_button_selector)
        finals_run_button.click()

        # Run finals (full or random)
        pool_page = PoolPage(self.browser, self.url)
        if full_mode:
            pool_page.run_pool()
        else:
            pool_page.run_pool_with_random_results()

    def playoff_running(self, full_mode):
        self.branches_order(full_mode)
        time.sleep(1)
        self.finals_running(full_mode)

    def swiss_running(self, full_mode):
        # Define rounds number based on the recommended value from the website
        rounds_number = self.find_element_wait(StagePageLocators.RECOMMEND_SWISS_ROUNDS_NUMBER)
        rounds_number = int(rounds_number.text)

        pool_page = PoolPage(self.browser, self.url)

        # Run every round (full or random)
        for x in range(rounds_number):
            self.click_button(StagePageLocators.SWISS_RUN_POOL_BUTTON)
            pool_page.run_swiss(full_mode)
            if x == rounds_number - 1:
                break
            self.click_button(StagePageLocators.BUILD_NEXT_SWISS_ROUND)
            time.sleep(0.5)
