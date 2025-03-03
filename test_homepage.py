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
        log.info("The page post first name is")
        home.get_mail().send_keys(data["mail"])
        log.info("Email entered:"+data["mail"])
        log.info("The page post email is")
        home.get_password().send_keys(data["password"])
        log.info("Password entered: "+data["password"])
        home.get_check().click()
        home.get_drop_down().click()
        log.info("Checkbox selected")
        log.info("The page post checkbox is")
        self.dropdown(home.get_drop_down(), data["gender"])
        log.info("Gender selected: "+data["gender"])
        log.info("The page post gender selection is")
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
        self.driver.refresh()
        log.info("Page refreshed")
        log.info("Assertion passed")
        driver.close()
        log.info("Driver closed")
        driver.quit()
        log.info("Driver quit")


    @pytest.fixture(params=home1.get_data())
    def data(self, request):
        return request.param
