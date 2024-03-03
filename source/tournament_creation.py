from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random
from selenium.webdriver.common.keys import Keys


def test_tournament_creation():
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
    #time.sleep(5)

    '''
    #закрываем алерт
    alert_btn = browser.find_element(By.CLASS_NAME, "cookies-alert__button")
    alert_btn.click()
    sign_btn = browser.find_element(By.CLASS_NAME, "btn.small")
    sign_btn.click()

    
    #переходим на турнирную страницу
    tournament_page_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > nav > div.user-block > div > div.body > ul > li:nth-child(3)')
    tournament_page_btn.click()
    '''

    #создаём турнир
    create_btn = browser.find_element(By.CLASS_NAME, 'svg-inline--fa.fa-plus')
    create_btn.click()
    #time.sleep(10)

    tournament_title = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(2) > div:nth-child(1) > input[type=text]')
    random_number = random.random()
    tournament_title.send_keys('test_tournament' + str(random_number))

    country = browser.find_element(By.CSS_SELECTOR, '#vs1__combobox > div.vs__selected-options > input')
    country.send_keys('Georgia' + Keys.ENTER)
    time.sleep(2)
    country.send_keys(Keys.ENTER)
    time.sleep(5)

    city = browser.find_element(By.CSS_SELECTOR, '#vs2__combobox > div.vs__selected-options > input')
    city.send_keys('Tbilisi')
    time.sleep(2)
    city.send_keys(Keys.ENTER)

    description = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(6) > textarea')
    description.send_keys('It is just another test tournament')

    save_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(9) > button')
    save_btn.click()

    assert browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > button')
