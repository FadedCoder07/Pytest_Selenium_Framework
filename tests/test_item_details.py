#bu proje POM(Page Object Model) ile düzenlendi
import time
from selenium.webdriver.common.by import By
import re
import pytest
from Pages.Anasayfa import Anasayfaa
from Pages.urun_sayfası import UrunDetaySayfası


@pytest.mark.usefixtures("setup")
class TestUrunDetails:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.anasayfa = Anasayfaa(self.driver)
    def test_add_item(self):
        self.driver.get(self.baseurl)


        self.anasayfa.first_item_click()

        urun_sayfası = UrunDetaySayfası(self.driver)

        before_number_of_products=urun_sayfası.number_of_items()
        quantity = int(urun_sayfası.give_quantity_numbers())

        urun_sayfası.add_to_cart_click()
        time.sleep(3)
        after_number_of_products = urun_sayfası.number_of_items()

        assert after_number_of_products== (quantity+before_number_of_products)

