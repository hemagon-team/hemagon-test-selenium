import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

load_dotenv()


@pytest.fixture(scope="function")
def browser(request):
    options_chrome = OptionsChrome()
    options_chrome.add_argument("--window-size=1920,1080")
    print("\nstart chrome browser for test...")
    if os.environ["DEV_ENV_MODE"] == 'remote':
        options_chrome.add_argument("--headless")
        browser = webdriver.Remote(os.environ["SELENIUM_HUB_URL"], options=options_chrome)
    else:
        browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options_chrome)
    yield browser
    print("\nquit browser...")
    browser.quit()
