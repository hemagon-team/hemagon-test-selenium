from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import random
from random import randint

def build_stage(self):
    btn_next_stage = self.browser.find_element(By.ID, 'btn-stage-0-build-next-stage')
    btn_next_stage.click()