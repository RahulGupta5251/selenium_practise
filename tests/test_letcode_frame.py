from pages.letcode_framepage import Letcode_framepage
import pytest
import time
@pytest.mark.usefixtures("setup_and_teardown")
class Test_letcode_frame:

    def test_enter_firstandlastname(self):
        frame_page = Letcode_framepage(self.driver)
        frame_page.launch_frame_page_url()
        frame_page.enter_first_and_last_name()


    def test_enter_email_address(self):
        frame_page = Letcode_framepage(self.driver)
        frame_page.launch_frame_page_url()
        frame_page.enter_email_address()
        time.sleep(4)
