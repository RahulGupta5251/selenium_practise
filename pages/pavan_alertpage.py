import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from configurations.URLs import URL

class Pavan_alertpage:

    def __init__(self,driver):
        self.driver =driver

    js_alert_xpath = "//*[@id='content']/div/ul/li[1]/button"
    js_confirm_xpath = "//*[@id='content']/div/ul/li[2]/button"
    js_prompt_xpath = "//*[@id='content']/div/ul/li[3]/button"

    def launch_pavan_alert_url(self):
        self.driver.get(URL.pavan_alert_url())

    def click_js_alert(self):
        self.driver.find_element(By.XPATH,self.js_alert_xpath).click()
        self.driver.switch_to.alert.accept()

    def click_js_alert_confirm_accept(self):
        self.driver.find_element(By.XPATH,self.js_confirm_xpath).click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)

    def click_js_alert_confirm_dismiss(self):
        self.driver.find_element(By.XPATH,self.js_confirm_xpath).click()
        self.driver.switch_to.alert.dismiss()
        time.sleep(3)

    def click_js_alert_prompt_accept(self):
        self.driver.find_element(By.XPATH,self.js_prompt_xpath).click()
        alert = self.driver.switch_to.alert
        alert.send_keys("my name is rahullll.....")
        alert.accept()
        time.sleep(3)

    def click_js_alert_prompt_dismiss(self):
        self.driver.find_element(By.XPATH,self.js_prompt_xpath).click()
        alert = self.driver.switch_to.alert
        alert.send_keys("my name is rahullll.....")
        alert.dismiss()
        time.sleep(3)

