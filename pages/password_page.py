import time
from selenium.common.exceptions import ElementClickInterceptedException
from .base_page import BasePage
from .locators import StagePageLocators
from .locators import LoginPageLocators
from .locators import PostalPageLocators
from .pool_page import PoolPage
from .fight_page import FightPage
from .pool_page import PoolPageLocators
from .fight_page import FightPageLocators
from selenium.webdriver.common.by import By
import random
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PasswordPage(BasePage):

    def ask_password_recovery_code(self, email):
        self.click_button(LoginPageLocators.PASSWORD_RECOVERY)
        self.fill_input(LoginPageLocators.PASSWORD_RECOVERY_EMAIL_FIELD, email)
        self.click_button(LoginPageLocators.GET_CODE_BUTTON)
    
    def get_recovery_code(self, postal_link, email, post_password):
        #enter the post
        self.browser.switch_to.new_window('tab')
        first_window = self.browser.window_handles[0]
        self.browser.get(postal_link)
        time.sleep(2)
        self.click_button(PostalPageLocators.LOGIN_PAGE_BUTTON)
        self.fill_input(PostalPageLocators.LOGIN_EMAIL, email)
        self.fill_input(PostalPageLocators.LOGIN_PASSWORD, post_password)
        self.click_button(PostalPageLocators.LOGIN_BUTTON)
        self.click_button(PostalPageLocators.LETTERS)
        self.click_button(PostalPageLocators.LETTER_CHOISE)
        
        #get the code from the letter
        message_text = self.find_element_wait(PostalPageLocators.MESSAGE)
        message_text = message_text.text
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        i = 0
        l = len(message_text) - 1
        code = ''
        while i <= l:
            if message_text[i] in numbers:
                code = code + message_text[i]
            i += 1
        self.browser.switch_to.window(first_window)
        return(code)
    
    def set_new_password(self, recovery_code):
        self.fill_input(LoginPageLocators.PASSWORD_RECOVERY_EMAIL_FIELD, recovery_code)
        self.click_button(LoginPageLocators.SEND_CODE_BUTTON)
        pass_field1 = self.find_element_wait(LoginPageLocators.ENTER_NEW_PASSWORD)
        pass_field2 = self.find_element_wait(LoginPageLocators.CONFIRM_NEW_PASSWORD)

        passwd_file = open('/home/thatsme/Git_working/hemagon-test-selenium/.env', 'r+')
        content = passwd_file.readlines()
        password = content[17]

        if 'TEST_USER_PASSWORD=HEMAhuema@1' in password:         
            pass_field1.send_keys('HEMAhuema@2')
            pass_field2.send_keys('HEMAhuema@2')
            content[17] = 'TEST_USER_PASSWORD=HEMAhuema@2\n'
            passwd_file.truncate(0)
            passwd_file.writelines(content)
        elif 'TEST_USER_PASSWORD=HEMAhuema@2' in password:
            pass_field1.send_keys('HEMAhuema@1')
            pass_field2.send_keys('HEMAhuema@1')
            content[17] = 'TEST_USER_PASSWORD=HEMAhuema@1\n'
            passwd_file.truncate(0)
            passwd_file.writelines(content)
        
        self.click_button(LoginPageLocators.SAVE_PASSWORD_BUTTON)

        time.sleep(3)