from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'https://hemagon.com'
link_tournament = 'https://hemagon.com/organizer/tournaments'

class TestTournamentView():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()
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
    
    #ТЕСТ переходим в обзор номинации
    def test_tournament_view_open(self):
        self.browser.get(link_tournament)
        self.browser.implicitly_wait(15)
        time.sleep(3)

        #переходим в турнир
        tournament_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div:nth-child(3) > div.tournaments > div:nth-child(1) > a > div.title')
        tournament_btn.click()
        time.sleep(3)

        #переходим на обзорную страницу турнира
        tourn_view_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(4) > a > svg')
        tourn_view_btn.click()
        time.sleep(1)

        #переходим на обзорную страницу номинации
        nom_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div.menu > div > div.nomination > a > div:nth-child(1)')
        nom_btn.click()
    
    #ТЕСТ смотрим, что есть бой
    def test_fight_presence(self):
        fights_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div.nomination > div:nth-child(3) > div > div > div > div > div.pool-title-line > button:nth-child(1)')
        fights_btn.click()
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div.nomination > div:nth-child(3) > div > div > div > div > div.pool-toggle-body > div > div:nth-child(1)')

    #ТЕСТ смотрим, что есть площадка
    def test_ring_presence(self):
        # заходим в бои, открываем площадки и копируем название площадки

        ring_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div.nomination > div:nth-child(3) > div > div > div > div > div.pool-title-line > div > button:nth-child(2)')
        ring_btn.click()
        ring_name = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div.nomination > div:nth-child(3) > div > div > div > div > div.pool-toggle-body > div > div:nth-child(1) > div.area')
        ring_name = ring_name.text

        #переходим в орговскую часть
        self.browser.get(link_tournament)
        time.sleep(1)
        tournament_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div:nth-child(3) > div.tournaments > div:nth-child(1) > a > div.title')
        tournament_btn.click()
        time.sleep(3)

        ring_adm_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(5)')
        ring_adm_btn.click()

        ring_adm_name = self.browser.find_element(By.CSS_SELECTOR, '#entity-64395be33bb3c474a0fd5c9a > td:nth-child(1)')
        ring_adm_name = ring_adm_name.text

        assert ring_name == ring_adm_name

    #ТЕСТ смотрим, что есть линк на трансляцию
    def test_link(self):
        stream_btn = self.browser.find_element(By.CSS_SELECTOR, '#entity-64395be33bb3c474a0fd5c9a > td:nth-child(2) > a')
        stream_btn.click()