from pages.pavan_alertpage import Pavan_alertpage
import time
import pytest



@pytest.mark.usefixtures("setup_and_teardown")
class Test_pavan_alert:

    def launch_pavan_alert_url(self):
        alert_url = Pavan_alertpage(self.driver)
        return alert_url.launch_pavan_alert_url()


    def test_pavan_js_alert(self):
        self.launch_pavan_alert_url()
        alert_page = Pavan_alertpage(self.driver)
        # alert_page.launch_pavan_alert_url()
        alert_page.click_js_alert()
        time.sleep(1)


    def test_pavan_js_confirm_alert_accept(self):
        self.launch_pavan_alert_url()
        alert_page = Pavan_alertpage(self.driver)
        alert_page.click_js_alert_confirm_accept()
        time.sleep(1)

    def test_pavan_js_confirm_alert_dismiss(self):
        self.launch_pavan_alert_url()
        alert_page = Pavan_alertpage(self.driver)
        alert_page.click_js_alert_confirm_dismiss()
        time.sleep(1)

    def test_pavan_js_prompt_alert_accept(self):
        self.launch_pavan_alert_url()
        alert_page =Pavan_alertpage(self.driver)
        alert_page.click_js_alert_prompt_accept()
        time.sleep(1)

    def test_pavan_js_prompt_alert_dismiss(self):
        self.launch_pavan_alert_url()
        alert_page =Pavan_alertpage(self.driver)
        alert_page.click_js_alert_prompt_dismiss()
        time.sleep(1)


