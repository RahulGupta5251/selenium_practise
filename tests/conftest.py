from selenium import webdriver
import pytest
from selenium.webdriver.ie.webdriver import WebDriver

from utilities.Readconfigurations import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config("basic_info","browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        print("please select valid webdriver chrome , edge or firefox...")
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()