import re
from selenium.webdriver.common.by import By
from Pages.PageBase import PageBase

class UrunDetaySayfası(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    URUN_SAYİSİ=(By.CSS_SELECTOR,"a.ico-cart span:nth-child(2)")
    URUN_ADET =(By.CSS_SELECTOR, "input[id$='EnteredQuantity']")
    SEPETE_EKLE=(By.CSS_SELECTOR, "input[id^='add-to-cart-button']")
    def number_of_items(self):
        number_of_products=self.driver.find_element(*UrunDetaySayfası.URUN_SAYİSİ).text
        number_of_products=re.findall(r'\d',number_of_products)
        before_number_of_products=int(number_of_products[0])
        return int(before_number_of_products)
    def give_quantity_numbers(self):
        quantity = self.driver.find_element(*UrunDetaySayfası.URUN_ADET).get_attribute('value')
        return int(re.findall(r'\d', quantity)[0])
    def add_to_cart_click(self):
        sepet_ekle=self.wait_element_visibility(UrunDetaySayfası.SEPETE_EKLE)
        sepet_ekle.click()

