from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys

def test_create_nomination():
    link_tournament = 'https://hemagon.com/organizer/tournaments'
    browser = webdriver.Chrome()
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

    #создаём площадку
    ring_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(5)')
    ring_btn.click()

    add_ring_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div.page-header > button')
    add_ring_btn.click()

    save_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)')
    save_btn.click()

    assert browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')

