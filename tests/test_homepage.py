from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
#POM kullanılmadan proje biraz daha karışık halde benzer bir proje olan ve POM kullanılan test_item_details'ı
# farkı göremk için inceleeybilirsin
@pytest.mark.usefixtures("setup")
class TestHomepage:
    def test_top_menu_items(self):

        self.driver.get("https://demowebshop.tricentis.com")
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]
        elements=self.driver.find_elements(By.CSS_SELECTOR,"ul.top-menu>li>a")

        actual_elements=[]

        for i in elements:
            actual_elements.append(i.text)

        for i in range(len(expected_menu)):
            assert expected_menu[i] == actual_elements[i]


    def test_finding_right_item(self):
        self.driver.get("https://demowebshop.tricentis.com")

        first_item_link=self.driver.find_element(By.CSS_SELECTOR,"div.product-item h2 a")
        item_name=first_item_link.text

        item_price=self.driver.find_element(By.CSS_SELECTOR,"span.price.actual-price").text
        first_item_link.click()

        item_name_detail=self.driver.find_element(By.CSS_SELECTOR,"div.product-name h1").text.strip()
        item_price_detail=self.driver.find_element(By.CSS_SELECTOR,"div.product-price span").text.strip()

        assert item_name==item_name_detail
        assert item_price==item_price_detail

