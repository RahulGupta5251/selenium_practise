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

  #thisis setupteardown 2 ### this is optimized way
# @pytest.fixture(scope="class")
# def setup_and_teardown():
#     browser = read_config("basic_info", "browser").lower()
#
#     browsers = {
#         "chrome": webdriver.Chrome,
#         "edge": webdriver.Edge,
#         "firefox": webdriver.Firefox
#     }
#
#     if browser not in browsers:
#         raise ValueError("Please select a valid browser: chrome, edge, or firefox.")
#
#     driver = browsers[browser]()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
#     yield driver  # Provide the driver instance to the test
#
#     driver.quit()