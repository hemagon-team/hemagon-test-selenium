import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome


@pytest.fixture(scope="function")
def browser(request):
    options_chrome = OptionsChrome()
    options_chrome.add_argument("--window-size=1920,1080")
    options_chrome.add_argument("--headless")
    print("\nstart chrome browser for test...")
    browser = webdriver.Remote(os.environ["SELENIUM_HUB_URL"], options=options_chrome)
    yield browser
    print("\nquit browser...")
    browser.quit()
