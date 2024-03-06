from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os

link = os.environ["TEST_BASEURL"]
link_tournament = link + '/organizer/tournaments'

class TestTournamentView():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        self.browser = webdriver.Remote(os.environ["SELENIUM_HUB_URL"], options=chrome_options)
        self.browser.implicitly_wait(15)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    #ТЕСТ логин
    def test_login(self):
        self.browser.get(link)
        self.browser.implicitly_wait(15)
        
        #закрываем уведомление
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
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > nav > div.user-block > div > div.trigger > div.name')
    
    #ТЕСТ переходим на страницу турнира и открываем пользовательскую страницу турнира
    def test_tournament_view_open(self):
        self.browser.get(link_tournament)
        self.browser.implicitly_wait(15)
        time.sleep(3)

        #переходим в турнир
        tournament_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div:nth-child(3) > div.tournaments > div:nth-child(1) > a > div.title')
        tournament_btn.click()
        time.sleep(3)

        #переходим на обзорную страницу турнира и смотрим наличие даты
        tourn_view_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(4) > a > svg')
        tourn_view_btn.click()
        time.sleep(1)
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div.dates')
    
    #ТЕСТ смотрим описание
    def test_description(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3)')

    #ТЕСТ смотрим сроки регистрации
    def test_registration_data(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(4)')
    
    #ТЕСТ смотрим название
    def test_tournament_name(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > h1')
    
    #ТЕСТ смотрим название номинации
    def test_nomination_name(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div.menu > div > div.weapon')

    #ТЕСТ проверяем наличие кликабельной ссылки на номинацию
    def test_nomination_click(self):
        nom_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div.menu > div > div.nomination > a > div:nth-child(1)')
        nom_btn.click()
