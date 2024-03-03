from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint

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


    #создаём номинацию
    nom_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(4)')
    nom_btn.click()
    create_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > button')
    create_btn.click()

    #название
    random_number = random.random()
    nom = 'Nomination№ ' + str(random_number)
    title = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > input[type=text]')
    title.send_keys(nom)

    #оружие
    i = 0
    weapon_number = randint(0, 24)
    weapon = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(2) > select')
    weapon.click()
    time.sleep(3)
    while i < weapon_number - 1:
        weapon.send_keys(Keys.ARROW_DOWN)
        i += 1
    weapon.send_keys(Keys.ENTER)

    #сохранение
    save_btn = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(2) > div > div > div:nth-child(5) > button')
    save_btn.click()
    time.sleep(5)

    nom_name = browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(1) > h5')
    assert nom_name.text == nom

test_create_nomination()