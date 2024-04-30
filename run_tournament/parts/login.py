from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint


def login(self):
    link = 'https://hemagon.com'
    link_tournament = 'https://hemagon.com/organizer/tournaments'
    loc = 'div.tournaments > div:nth-child(1)'
    
    self.browser.get(link)
    self.browser.implicitly_wait(15)
        
    cookies_btn = self.browser.find_element(By.CLASS_NAME, "cookies-alert__button")
    cookies_btn.click()
    
    time.sleep(1)

    sign_btn = self.browser.find_element(By.CLASS_NAME, "btn.small")
    sign_btn.click()
    email = self.browser.find_element(By.ID, "input-email")
    email.send_keys('paulus.mair@mailfence.com')
    password = self.browser.find_element(By.ID, "input-password")
    password.send_keys('HEMAhuema@1')
    accept_btn = self.browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    accept_btn.click()
    time.sleep(3)

    self.browser.get(link_tournament)
    self.browser.fullscreen_window()

    tourn_btn = self.browser.find_element(By.CSS_SELECTOR, loc)
    tourn_btn.click()
    time.sleep(1)
    nom_btn = self.browser.find_element(By.ID, 'tournament-menu-nominations')
    nom_btn.click()
    time.sleep(1)

    choose_category_btn = self.browser.find_element(By.CSS_SELECTOR, 'div.organizer-tournament > div:nth-child(1) div:nth-child(1) > a')
    choose_category_btn.click()
    time.sleep(1)
    stages_btn = self.browser.find_element(By.ID, 'nomination-menu-stages')
    stages_btn.click()
    time.sleep(3)