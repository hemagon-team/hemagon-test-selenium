from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as OptionsChrome


@pytest.fixture(scope="function")
def browser(request):
    options_chrome = OptionsChrome()
    print("\nstart chrome browser for test...")
    browser = webdriver.Chrome(options=options_chrome)
    yield browser
    print("\nquit browser...")
    browser.quit()
