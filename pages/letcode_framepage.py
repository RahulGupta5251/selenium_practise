from selenium.webdriver.common.by import By

from configurations.URLs import URL
from pages.Basepage import Basepage


class Letcode_framepage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)


    first_name_textbox_xpath = "/html/body/app-root/app-frame-content/div/div/form/div[1]/div/input"
    last_name_textbox_xpath = "/html/body/app-root/app-frame-content/div/div/form/div[2]/div/input"
    email_address_xpath = "/html/body/app-root/app-innerframe/div/div/div/div/div/input"

    def launch_frame_page_url(self):
        self.driver.get(URL.frame_url())


    def enter_first_and_last_name(self):
        self.driver.switch_to.frame("firstFr")
        self.type_to_element("Rahul.....","first_name_textbox_xpath",self.first_name_textbox_xpath)
        self.type_to_element("Gupta....","last_name_textbox_xpath",self.last_name_textbox_xpath)


    def enter_email_address(self):
        self.driver.switch_to.frame("firstFr")
        self.driver.switch_to.frame(1)
        # self.type_to_element("Rahul.@gmail.com....","email_address_xpath",self.email_address_xpath)
        self.driver.find_element(By.XPATH,self.email_address_xpath).send_keys("Rahul.@gmail.com....")
