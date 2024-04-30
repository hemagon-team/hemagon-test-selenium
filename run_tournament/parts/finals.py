from selenium import webdriver
from selenium.webdriver.common.by import By 
from parts.run_pool import run_pool   
def finals(self):
    finals = self.browser.find_elements(By.ID, 'btn-stage-1-side-0-run-playoff-round')
    finals = len(finals)
    finals = 'div.rounds-container.eliminations > div:nth-child(' + str(finals) + ') > div:nth-child(2) > div:nth-child(1) > a > #btn-stage-1-side-0-run-playoff-round'
    finals = self.browser.find_element(By.CSS_SELECTOR, finals)
    finals.click()
    run_pool(self)