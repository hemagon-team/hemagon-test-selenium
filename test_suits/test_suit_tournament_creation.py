from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint
import os

link = os.environ["TEST_BASEURL"]
link_tournament = link + '/organizer/tournaments'

class TestTournamentCreation():

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

    #ТЕСТ создаём турнир
    def test_tournament_creation(self):
        self.browser.get(link_tournament)
        self.browser.implicitly_wait(15)
        create_btn = self.browser.find_element(By.CLASS_NAME, 'svg-inline--fa.fa-plus')
        create_btn.click()

        #название турнира
        tournament_title = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(2) > div:nth-child(1) > input[type=text]')
        random_number = random.random()
        tournament_title.send_keys('test_tournament' + str(random_number))

        #страна и город
        country = self.browser.find_element(By.CSS_SELECTOR, '#vs1__combobox > div.vs__selected-options > input')
        country.send_keys('Georgia' + Keys.ENTER)
        time.sleep(2)
        country.send_keys(Keys.ENTER)
        time.sleep(5)

        city = self.browser.find_element(By.CSS_SELECTOR, '#vs2__combobox > div.vs__selected-options > input')
        city.send_keys('Tbilisi')
        time.sleep(2)
        city.send_keys(Keys.ENTER)

        #описание и сохранение
        description = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(6) > textarea')
        description.send_keys('It is just another test tournament')

        save_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(9) > button')
        save_btn.click()
        time.sleep(5)

        time.sleep(2)
        assert self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > button')
        

    #ТЕСТ создаём номинацию
    def test_nomination_creation(self):
        #создаём номинацию
        nom_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(4)')
        nom_btn.click()
        create_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > button')
        create_btn.click()

        #название
        random_number = random.random()
        nom = 'Nomination№ ' + str(random_number)
        title = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > input[type=text]')
        title.send_keys(nom)
        time.sleep(2)

        #оружие
        '''
        i = 0
        weapon_number = randint(0, 10)
        weapon = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(2) > select')
        weapon.click()
        time.sleep(3)
        while i < weapon_number - 1:
            weapon.send_keys(Keys.ARROW_DOWN)
            i += 1
        weapon.send_keys(Keys.ENTER)
        '''
        weapon = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(2) > select')
        weapon.click()
        weapon.send_keys(Keys.ARROW_DOWN)
        weapon.send_keys(Keys.ENTER)

        #сохранение
        save_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(9) > button')
        save_btn.click()
        time.sleep(5)
        '''

        nom_name = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(1) > h5')
        assert nom_name.text == nom
        '''
    '''
    #ТЕСТ добавляем этап
    def test_stage_creation(self):
        stages_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(4)')
        stages_btn.click()
        time.sleep(3)
        addstage_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > button')
        addstage_btn.click()
        time.sleep(3)
        pool_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div:nth-child(2) > div > label:nth-child(1)')
        pool_btn.click()
        time.sleep(3)
        save_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div:nth-child(6) > button:nth-child(2)')
        save_btn.click()
        assert self.browser.find_element(By.CLASS_NAME, 'notification-content')
    
        #ТЕСТ добавляем участников
    def test_add_participants(self):
        part_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(3)')
        part_btn.click()
        time.sleep(2)
        enroll_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > button:nth-child(2)')
        enroll_btn.click()
        time.sleep(2)
        full_approve_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > button:nth-child(3)')
        full_approve_btn.click()
        time.sleep(5)
        num_enrolled = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div:nth-child(1) > select > option:nth-child(1)')
        num_enrolled = num_enrolled.text

        #проверяем что всё ок
        stage_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div.organizer-tournament-menu > a:nth-child(4)')
        stage_btn.click()
        time.sleep(2)
        num_accepted = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.users > div.inline-block.users-count')
        num_accepted = num_accepted.text
        assert num_enrolled == num_accepted
    '''
    '''
    #ТЕСТ редактируем этап
    def test_stage_edit(self):
        self.browser.implicitly_wait(15)
        random_num = randint(8, 16)
        edit_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.stage-content > div:nth-child(2) > button')
        edit_btn.click()      
        proceed_num = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div:nth-child(3) > div > input[type=number]')
        proceed_num.send_keys(Keys.BACKSPACE)
        proceed_num.send_keys(str(random_num))
        #proceed_num.send_keys(Keys.ENTER)

        save_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div:nth-child(5) > button:nth-child(2)')
        save_btn.click()

        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')

        time.sleep(4)
    '''
    '''
    #ТЕСТ добавляем пулы
    def test_pool_creation(self):
        self.browser.implicitly_wait(15)
        pool_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.stage-content > div:nth-child(4) > button')
        pool_btn.click()
        time.sleep(3)

        assert self.browser.find_element(By.CLASS_NAME, 'notification-content')
    
    #ТЕСТ отправляем участников в пул
    def test_seed(self):
        time.sleep(2)
        seed_btn = self.browser.find_element(By.CSS_SELECTOR,'#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div > div:nth-child(3) > div > div > div > div > div.stage-content > div:nth-child(4) > button:nth-child(2)')
        seed_btn.click()
        assert self.browser.find_element(By.CLASS_NAME, 'notification-content')


    #ТЕСТ добавляем площадку
    def test_ring_creation(self):
        self.browser.implicitly_wait(15)

        ring_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(5) > a:nth-child(5)')
        ring_btn.click()

        add_ring_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div.page-header > button')
        add_ring_btn.click()

        save_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)')
        save_btn.click()

        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')
    '''
    ''' 
    #ТЕСТ удаляем площадку
    def test_ring_deletion(self):
        self.browser.implicitly_wait(15)

        remove_btn = self.browser.find_element(By.CLASS_NAME, 'svg-inline--fa.fa-xmark')
        remove_btn.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')
    '''
