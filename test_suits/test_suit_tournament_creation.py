from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint

#Shalom, orthanc bronadui! 222

link = 'https://hemagon.com'
link_tournament = 'https://hemagon.com/organizer/tournaments'

# test test

#это переменная для количества участников. В силу убогости автора она нужна как глобальная
num_accepted = 0
#то же самое для пулов
num_pool = 0

class TestTournamentCreation():

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
        assert self.browser.find_element(By.CLASS_NAME, 'name')

    #ТЕСТ создаём турнир
    def test_tournament_creation(self):
        self.browser.get(link_tournament)
        self.browser.implicitly_wait(15)
        create_btn = self.browser.find_element(By.ID, 'btn-create-tournament')
        create_btn.click()

        #название турнира
        tournament_title = self.browser.find_element(By.ID, 'input-tournament-title')
        random_number = random.random()
        tournament_title.send_keys('test_tournament' + str(random_number))

        #страна и город
        country = self.browser.find_element(By.CSS_SELECTOR, '#vs1__combobox > div.vs__selected-options > input')
        #country.click()
        #time.sleep(2)
        country.send_keys('Georgia' + Keys.ENTER)
        time.sleep(2)
        country.send_keys(Keys.ENTER)
        time.sleep(5)

        city = self.browser.find_element(By.CSS_SELECTOR, '#vs2__combobox > div.vs__selected-options > input')
        city.click()
        city.send_keys('Tbilisi')
        time.sleep(2)
        city.send_keys(Keys.ENTER)

        #описание и сохранение
        description = self.browser.find_element(By.ID, 'input-tournament-description')
        description.send_keys('It is just another test tournament')

        save_btn = self.browser.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div:nth-child(9) > button')
        save_btn.click()
        time.sleep(2)
        assert self.browser.find_element(By.ID, 'tournament-menu-overview')
        

    #ТЕСТ создаём номинацию
    def test_nomination_creation(self):
        #создаём номинацию
        nom_btn = self.browser.find_element(By.ID, 'tournament-menu-nominations')
        nom_btn.click()
        create_btn = self.browser.find_element(By.ID, 'btn-nomination-add')
        create_btn.click()

        #название
        random_number = random.random()
        nom = 'Nomination№ ' + str(random_number)
        title = self.browser.find_element(By.ID, 'input-nomination-title')
        title.send_keys(nom)
        time.sleep(2)

        #оружие
        weapon = self.browser.find_element(By.ID, 'input-nomination-weapon')
        weapon.click()
        weapon.send_keys(Keys.ARROW_DOWN)
        weapon.send_keys(Keys.ENTER)

        #сохранение
        save_btn = self.browser.find_element(By.ID, 'btn-nomination-save')
        save_btn.click()
        time.sleep(5)

      
        #ТЕСТ добавляем участников
    def test_add_participants(self):
        part_btn = self.browser.find_element(By.ID, 'nomination-menu-participants')
        part_btn.click()
        time.sleep(2)
        enroll = self.browser.find_element(By.ID, 'input-requests-test-enroll-number')
        rr = random.randint(0, 5)
        i = 0
        enroll.click()
        while i < rr:
            enroll.send_keys(Keys.ARROW_DOWN)
            i+= 1
        enroll.send_keys(Keys.ENTER)
        enroll_btn = self.browser.find_element(By.ID, 'btn-requests-test-enroll')
        enroll_btn.click()
        time.sleep(5)
        full_approve_btn = self.browser.find_element(By.ID, 'input-requests-test-full-approve')
        full_approve_btn.click()
        confirm = self.browser.switch_to.alert
        confirm.accept()
        time.sleep(10)
        num_enrolled = self.browser.find_element(By.ID, 'requests-stats-requests')
        num_enrolled = int(num_enrolled.text)
        global num_accepted
        num_accepted = self.browser.find_element(By.ID, 'requests-stats-accepted')
        num_accepted = int(num_accepted.text)
        assert num_enrolled == num_accepted
        time.sleep(2)

    #ТЕСТ добавляем этап с пулами
    def test_pool_stage_creation(self):
        stages_btn = self.browser.find_element(By.ID, 'nomination-menu-stages')
        stages_btn.click()
        time.sleep(3)
        addstage_btn = self.browser.find_element(By.ID, 'btn-stage-add')
        addstage_btn.click()
        time.sleep(3)
        pool_btn = self.browser.find_element(By.ID, 'input-stage-type-POOL')
        pool_btn.click()
        time.sleep(3)
        global num_accepted
        num_next_stage = num_accepted // 2
        field_next_stage = self.browser.find_element(By.ID, 'input-stage-outputCount-num')
        field_next_stage.click()
        field_next_stage.send_keys(Keys.CONTROL + 'a')
        field_next_stage.send_keys(Keys.CLEAR)
        field_next_stage.send_keys(num_next_stage)
        save_btn = self.browser.find_element(By.ID, 'btn-stage-editing-save')
        save_btn.click()
        assert self.browser.find_element(By.CLASS_NAME, 'notification-content')

    #ТЕСТ добавляем этап плейоф
    def test_playoff_stage_creation(self):
        addstage_btn = self.browser.find_element(By.ID, 'btn-stage-add')
        addstage_btn.click()
        time.sleep(3)
        playoff_btn = self.browser.find_element(By.ID, 'input-stage-type-ELIMINATION')
        playoff_btn.click()
        save_btn = self.browser.find_element(By.ID, 'btn-stage-editing-save')
        save_btn.click()
        assert self.browser.find_element(By.CLASS_NAME, 'notification-content')
    
    #ТЕСТ добавляем пулы
    def test_pool_creation(self):
        self.browser.implicitly_wait(15)
        i = 0
        global num_pool
        global num_accepted
        pool_btn = self.browser.find_element(By.ID, 'btn-stage-0-add-pool')
        if num_accepted % 7 != 0:
            num_pool = num_accepted // 7 + 1
        else:
            num_pool = num_accepted // 7
        while i < num_pool:
            pool_btn.click()
            i += 1
            time.sleep(4)
        #assert self.browser.find_element(By.CLASS_NAME, 'notification-content')
    
    #ТЕСТ отправляем участников в пул
    def test_seed(self):
        time.sleep(2)
        seed_btn = self.browser.find_element(By.ID, 'btn-stage-0-seed')
        seed_btn.click()
        assert self.browser.find_element(By.CLASS_NAME, 'notification-content')


    #ТЕСТ добавляем площадку
    def test_ring_creation(self):
        self.browser.implicitly_wait(15)

        ring_btn = self.browser.find_element(By.ID, 'tournament-menu-areas')
        ring_btn.click()
        time.sleep(4)
        add_ring_btn = self.browser.find_element(By.ID, 'btn-area-add')
        add_ring_btn.click()
        time.sleep(4)
        save_btn = self.browser.find_element(By.ID, 'btn-area-save')
        save_btn.click()

        assert self.browser.find_element(By.CLASS_NAME, 'vue-notification-template.vue-notification.success')

    