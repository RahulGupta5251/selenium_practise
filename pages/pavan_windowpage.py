from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class Pavan_window_page:
    def __init__(self,driver):
        self.driver = driver

    orange_url = "https://opensource-demo.orangehrmlive.com/"
    demo_button_xpath = "//*[@id='navbarSupportedContent']/div[2]/ul/li[1]/a/button"
    amazon_url = "https://www.amazon.in/"
    flipkart_url = "https://www.flipkart.com/"
    nopcommerce_url = "https://demo.nopcommerce.com/"

    def launch_orange_hrm_url(self):
        self.driver.get(self.orange_url)


    def click_orange_hrm_link(self):
        self.driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
        time.sleep(4)

    def launch_nop_orange_url(self):
        self.driver.get(self.nopcommerce_url)

    def click_register_button_by_keyboard(self):
        keyss = Keys.CONTROL + Keys.RETURN
        self.driver.find_element(By.LINK_TEXT,"Register").send_keys(keyss)
        time.sleep(5)


