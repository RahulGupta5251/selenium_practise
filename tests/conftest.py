from selenium import webdriver
import pytest

@pytest.fixture()
def setup_and_teardown(request):

    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()