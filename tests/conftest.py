import requests
from queries.users import query_string_login, variables_login_nl, variables_for_admin, variables_login_est
import pytest
from utils.helper import EntySession
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def setup_browser():
    browser.config.window_height = 1200
    browser.config.window_width = 1500
    browser.config.timeout = 40.0
    browser.config.wait_for_no_overlap_found_by_js = True
    options = Options()

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '100.0',
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)

    s_login = os.getenv('LOGIN_QG')
    s_password = os.getenv('PASSWORD_QG')

    driver = webdriver.Remote(
        command_executor=f"https://{s_login}:{s_password}@selenoid.autotests.cloud/wd/hub",
        # command_executor="https://dev-webhooks.enty.io/wd/hub/",
        options=options,
    )
    browser.config.driver = driver
    browser.config.base_url = os.getenv('DEV_SIGN_UP_LINK')

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="function")
def login_nl():
    url = "https://dev.enty.io/api"
    response = requests.post(url=url, json={'query': query_string_login, 'variables': variables_login_nl})
    token = response.json()['data']['user']['login']['sid']
    return token


@pytest.fixture(scope="function")
def login_est():
    url = "https://dev.enty.io/api"
    response = requests.post(url=url, json={'query': query_string_login, 'variables': variables_login_est})
    token = response.json()['data']['user']['login']['sid']
    return token


@pytest.fixture(scope="function")
def login_as_admin():
    url = "https://dev.enty.io/api"
    response = requests.post(url=url, json={'query': query_string_login, 'variables': variables_for_admin})
    token = response.json()['data']['user']['login']['sid']
    return token


@pytest.fixture(scope="function")
def login_as_admin():
    url = "https://dev.enty.io/api"
    response = requests.post(url=url, json={'query': query_string_login, 'variables': variables_for_admin})
    token = response.json()['data']['user']['login']['sid']
    return token


@pytest.fixture(scope="session")
def prerelease_session():
    return EntySession(base_url=os.getenv('PRERELEASE_API_LINK'))


@pytest.fixture(scope="session")
def dev_session():
    return EntySession(base_url=os.getenv('DEV_API_LINK'))
