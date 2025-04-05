import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)
    all_links = driver.find_elements(By.TAG_NAME,"a")
    time.sleep(5)
    for link in all_links:
        url = link.get_attribute("href")
        res = requests.head(url)
        if res.status_code>=400:
            print("url is broken link is >>> ", url)
    driver.quit()
