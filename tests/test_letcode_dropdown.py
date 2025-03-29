from pages.letcode_dropdown_Page import LetcodeDropdownpage

import pytest
import time

@pytest.mark.usefixtures("setup_and_teardown")
class Test_letcdoe_dropdown:


    def test_select_fruit_dropdown(self):
       dropdown_page = LetcodeDropdownpage(self.driver)
       dropdown_page.launch_letcode_dropdown_url()
       dropdown_page.click_fruit_dropdown()
       time.sleep(3)

    def test_select_superhero_dropdwon(self):
        dropdown_page = LetcodeDropdownpage(self.driver)
        dropdown_page.launch_letcode_dropdown_url()
        dropdown_page.select_superherodropdwon()
        time.sleep(3)

    def test_select_programming_dropdwon(self):
        dropdown_page = LetcodeDropdownpage(self.driver)
        dropdown_page.launch_letcode_dropdown_url()
        dropdown_page.select_programming_option()
        time.sleep(3)

    def test_select_country_dropdown(self):
        dropdown_page = LetcodeDropdownpage(self.driver)
        dropdown_page.launch_letcode_dropdown_url()
        dropdown_page.select_country_option()
        time.sleep(4)

