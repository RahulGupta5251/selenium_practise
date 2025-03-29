from pages.pavan_windowpage import Pavan_window_page
import time
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class Test_pavan_window_page:

    # def test_orangehrm_with_switch_pages(self):
    #     window_page = Pavan_window_page(self.driver)
    #     window_page.launch_orange_hrm_url()
    #     window_page.click_orange_hrm_link()
    #     ids = self.driver.window_handles
    #     for i in ids:
    #         self.driver.switch_to.window(i)
    #         if self.driver.title =="OrangeHRM":
    #             self.driver.close()
    #
    #     time.sleep(5)

    # def test_opnopcommerce_click_register_open_newtab(self):
    #     window_page = Pavan_window_page(self.driver)
    #     window_page.launch_nop_orange_url()
    #     window_page.click_register_button_by_keyboard()
    #     time.sleep(4)

    def test_launch_multiple_url_in_multiple_tabss(self):
        self.driver.get("https://www.amazon.in/")
        self.driver.switch_to.new_window("tab")
        self.driver.get("https://www.flipkart.com/")
        self.driver.switch_to.new_window("tab")
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.switch_to.new_window("tab")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(6)
        ids = self.driver.window_handles
        for i in ids:
            self.driver.switch_to.window(i)
            if self.driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!":
                self.driver.close()
                time.sleep(5)