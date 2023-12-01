import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import PageNotOpenedExeption
from ui.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']

    with allure.step('Init browser'):
        browser = get_driver(config)
        browser.get(url)

    yield browser
    browser.quit()


def get_driver(config):
    browser_name = config['browser']

    if browser_name == 'chrome':
        options = Options()
        browser = webdriver.Chrome(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='session')
def credentials(repo_root):
    with open(os.path.join(repo_root, 'files/userdata'), 'r') as f:
        lines = f.readlines()

    email = lines[0].strip()
    password = lines[1].strip()

    return email, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config)
    driver.get(config['url'])
    login_page = LoginPage(driver)

    try:
        login_page.login(*credentials)
    except PageNotOpenedExeption:
        if 'login?&fail=1' in driver.current_url:
            login_page.confirm_login(*credentials)
        else:
            raise

    cookies = driver.get_cookies()
    driver.quit()

    return cookies
