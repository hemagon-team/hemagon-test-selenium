from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os

link = os.environ["TEST_BASEURL"]
link_tournament = link + '/organizer/tournaments'

def test_squad():
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
    time.sleep(3)

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

    # переходим к участникам и записывам тестовую пачку
    part_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(3)')
    part_btn.click()
    time.sleep(2)
    enroll_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > button:nth-child(2)')
    enroll_btn.click()
    time.sleep(2)
    full_approve_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > button:nth-child(3)')
    full_approve_btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(5)
    num_enrolled = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > select > option:nth-child(1)')
    num_enrolled = num_enrolled.text

    #проверяем что всё ок
    stage_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(4)')
    stage_btn.click()
    num_accepted = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.users > div.inline-block.users-count')
    num_accepted = num_accepted.text
    assert num_enrolled == num_accepted
