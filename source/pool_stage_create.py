from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os

link = os.environ["TEST_BASEURL"]
link_tournament = link + '/organizer/tournaments'

def test_stage_pool():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    self.browser = webdriver.Remote(os.environ["SELENIUM_HUB_URL"], options=chrome_options)
    browser.get(link_tournament)
    browser.implicitly_wait(15)

    #логинимся
    email = browser.find_element(By.ID, "input-email")
    email.send_keys('paulus.mair@mailfence.com')
    password = browser.find_element(By.ID, "input-password")
    password.send_keys('HEMAhuema@1')
    
    accept_btn = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
    accept_btn.click()

    #выбираем турнир
    choose_tournament = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div:nth-child(3) > div.tournaments > div > a')
    choose_tournament.click()
     
    #закрываем алерт
    alert_btn = browser.find_element(By.CLASS_NAME, "cookies-alert__button")
    alert_btn.click()
    sign_btn = browser.find_element(By.CLASS_NAME, "btn.small")
    sign_btn.click()

    #выбираем номинацию
    nom_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(4)')
    nom_btn.click()
    choose_nomination = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div > a')
    choose_nomination.click()
    time.sleep(3)

    #создаём этап
    stage_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(4)')
    stage_btn.click()
    time.sleep(3)
    addstage_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > button')
    addstage_btn.click()
    time.sleep(3)
    pool_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > label:nth-child(1)')
    pool_btn.click()
    time.sleep(3)
    save_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div:nth-child(7) > button:nth-child(2)')
    save_btn.click()

    assert browser.find_element(By.CLASS_NAME, 'notification-content')
