from selenium.webdriver.common.by import By
from utilities.Baseclass import Baseclass
from Page_Objects.HomePage import Home

from conftest import driver


class Test_First(Baseclass):
    def test_first(self):
        log = self.get_logger()
        # Land on shopping cart page
        home = Home(self.driver)
        checkout = home.shop_item()
        log.info("Getting the info from the shopping page")
        # Add items to cart
        product = checkout.get_card_titles()
        for i in product:
            log.info(i.text)
            if i.text == "Blackberry":
                checkout.get_card_footer().click()
                break
        log.info("Item added to cart")
        # Go to cart
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        checkout.get_cart_btn().click()
        log.info("Navigated to checkout page")
        # Click on checkout
        confirm = checkout.get_checkout_btn()
        log.info("Navigated to confirm page")
        # Enter country, click on checkbox and click on purchase
        confirm.get_country().send_keys("ind")
        self.exp_wait("India")
        confirm.get_select_country().click()
        log.info("Country selected")
        confirm.get_checkbox().click()
        log.info("Checkbox selected")
        confirm.get_purchase().click()
        log.info("Purchased")
        # Verify a success message
        self.success()
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        text_match = confirm.get_text().text
        log.info("Text received: " + text_match)
        assert "Thank you!" in text_match
        log.info("Test completed")
        self.driver.refresh()
        log.info("Page refreshed")
        log.info("Assertion passed")
        driver.close()
        log.info("Driver closed")
        driver.quit()
        log.info("Driver quit")

