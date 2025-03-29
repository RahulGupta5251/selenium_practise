from typing import final

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from configurations.URLs import URL
from pages.Basepage import Basepage


class LetcodeDropdownpage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    fruit_dropdown_button_xpath = "//*[@id='fruits']"
    superman_dropdown_xpath = "//*[@id='superheros']"
    programming_language_xpath = "//*[@id='lang']"
    country_dropdown_xpath = "//*[@id='country']"


    def launch_letcode_dropdown_url(self):
        self.driver.get(URL.dropdown_url())

    def Dropdown(self,element):
        return Select(element)

    def click_fruit_dropdown(self):
        element = self.get_element("fruit_dropdown_button_xpath",self.fruit_dropdown_button_xpath)
        opt  = self.Dropdown(element)
        opt.select_by_visible_text("Banana")

    def select_superherodropdwon(self):
        element = self.get_element("superman_dropdown_xpath",self.superman_dropdown_xpath)
        opt = self.Dropdown(element)
        opt.select_by_value("dd")

    def select_programming_option(self):
        element = self.get_element("programming_language_xpath",self.programming_language_xpath)
        opt = self.Dropdown(element)
        alloptions = opt.options
        for i in alloptions:
            print(i.text)
        opt.select_by_index(len(alloptions)-1)

    def select_country_option(self):
        element = self.driver.find_element(By.XPATH,self.country_dropdown_xpath)
        opt = self.Dropdown(element)
        opt.select_by_visible_text("India")