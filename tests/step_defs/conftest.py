import json
import pytest
import os
from pages.uploadPage import UploadPage
from pytest_bdd import given
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Fixture   
@pytest.fixture
def target_env(scope='session'):
  config_path = os.environ['TARGET_ENV']
  with open(config_path) as config_file:
    config_data = json.load(config_file)
  return config_data

# Fixture
@pytest.fixture
def browser(target_env):
    if target_env['browser'] == 'chrome':
        opts = webdriver.ChromeOptions()
        if target_env['headless']:
            opts.add_argument('headless')
        b = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    elif target_env['browser'] == 'firefox':
        opts = webdriver.FirefoxOptions()
        if target_env['headless']:
            opts.add_argument('-headless')
        b = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    else:
        raise Exception(f'Browser "{target_env["browser"]}" is not supported')
    
    b.implicitly_wait(target_env['implicit_wait'])
    b.maximize_window()

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()
    
# Shared Given Steps
@given('the Guru99 Demo home page is displayed', target_fixture='upload_page')
def upload_page(browser, target_env):
    uploadPage = UploadPage(browser)
    uploadPage.go_to(target_env['baseUrl'])
    return uploadPage