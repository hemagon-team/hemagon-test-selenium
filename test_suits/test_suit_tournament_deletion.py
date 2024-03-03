from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint

link = 'https://hemagon.com'
link_tournament = 'https://hemagon.com/organizer/tournaments'

class TestTournamentDeletion():

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
    
    #ТЕСТ переходим на страницу турнира и удаляем площадку
    def test_ring_deletion(self):
        self.browser.get(link_tournament)
        self.browser.implicitly_wait(15)
        time.sleep(3)
        #переходим в турнир
        tournament_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div:nth-child(3) > div.tournaments > div:nth-child(1) > a > div.title')
        tournament_btn.click()
        time.sleep(3)

        #переходим в площадки
        ring_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(5)')
        ring_btn.click()
        time.sleep(3)

        remove_btn = self.browser.find_element(By.CLASS_NAME, 'svg-inline--fa.fa-xmark')
        remove_btn.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')
    
    #ТЕСТ удаляем пулы
    def test_pool_deletion(self):
        self.browser.implicitly_wait(15)

        #переходим в номинации
        nom_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(4)')
        nom_btn.click()
        time.sleep(1)

        act_nom_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div > a')
        act_nom_btn.click()
        time.sleep(1)

        #переходим в этапы
        stage_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(4)')
        stage_btn.click()
        time.sleep(1)
        #удаляем пул
        pool_remove_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.stage-content > div.rounds-container.pools > div > div > div > div:nth-child(3) > button:nth-child(3)')
        pool_remove_btn.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')


    #ТЕСТ удаляем этап
    def test_stage_deletion(self):

        stage_remove_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.stage-content > div:nth-child(1) > button')
        stage_remove_btn.click()

        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')
        time.sleep(3)

    #ТЕСТ удаляем номинацию
    def test_nom_deletion(self):
        time.sleep(3)
        nom_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(1)')
        nom_btn.click()
        time.sleep(1)

        nom_remove_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(4) > button')
        nom_remove_btn.click()

        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')

    #ТЕСТ удаляем турнир
    def test_tournament_deletion(self):
        view_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(1)')
        view_btn.click()
        time.sleep(1)

        tourn_remove_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > button')
        tourn_remove_btn.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')
