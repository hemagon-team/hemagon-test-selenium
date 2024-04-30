from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from parts.run_left import run_left
from parts.run_right import run_right


def branches(self):
    choose_branch = randint(0, 1)
    if choose_branch == 0:
        run_left(self)
        run_right(self)

    else:
        run_left(self)
        run_right(self)
    
    next_playoff_button = self.browser.find_element(By.ID, 'btn-stage-1-build-next-round-playoff')
    next_playoff_button.click()