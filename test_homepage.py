import pytest
from Page_Objects.HomePage import Home
from Testdata.Home_page_data import home1

from utilities.Baseclass import Baseclass

class Test_Home(Baseclass):
    def test_form(self, data):
        log = self.get_logger()
        home = Home(self.driver)
        home.get_name().send_keys(data["first_name"])
        log.info("First name entered: "+data["first_name"])
        # home.get_mail().send_keys(data["mail"])
        # log.info("Email entered: "+data["mail"])
        # home.get_password().send_keys(data["password"])
        # log.info("Password entered: "+data["password"])
        home.get_check().click()
        log.info("Checkbox selected")
        self.dropdown(home.get_drop_down(), data["gender"])
        log.info("Gender selected: "+data["gender"])
        home.get_radio().click()
        log.info("Radio button selected")
        log.info("The page post radio button is")
        home.get_submit().click()
        log.info("Submit button clicked")
        log.info("The page post submit button is")
        message_conf = home.get_alert_text().text
        log.info("Alert message captured is:" + message_conf)
        self.driver.refresh()
        assert "Success" in message_conf
        log.info("Page refreshed")
        log.info("Test completed")
        log.info("Test completed!!!")



    @pytest.fixture(params=home1.get_data())
    def data(self, request):
        return request.param
