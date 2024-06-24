import time
from selenium.webdriver.common.by import By
import re
import pytest

@pytest.mark.usefixtures("setup")
class TestUrunDetails:
    def test_add_item(self):
        self.driver.get("https://demowebshop.tricentis.com")
        self.driver.find_element(By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]").click()

        number_of_products=self.driver.find_element(By.CSS_SELECTOR,"a.ico-cart span:nth-child(2)").text
        number_of_products=re.findall(r'\d',number_of_products)
        before_number_of_products=int(number_of_products[0])

        quantity=self.driver.find_element(By.CSS_SELECTOR,"input[id$='EnteredQuantity']").get_attribute('value')
        quantity = int(re.findall(r'\d', quantity)[0])

        self.driver.find_element(By.CSS_SELECTOR,"input[id^='add-to-cart-button']").click()
        time.sleep(2)

        number_of_products = self.driver.find_element(By.CSS_SELECTOR, "a.ico-cart span:nth-child(2)").text
        number_of_products = re.findall(r'\d', number_of_products)
        after_number_of_products = int(number_of_products[0])

        assert after_number_of_products== (quantity+before_number_of_products)

