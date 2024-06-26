from selenium.webdriver import Keys
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.PageBase import PageBase


class AramaSayfasi(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ARAMA_KUTUSU = ARAMA_KUTUSU = (By.ID, "small-searchterms")
    ARAMA_UYARI_MESAJI = (By.CSS_SELECTOR, "div.search-results")
    ARANAN_URUNLER = (By.CSS_SELECTOR, "div.product-item h2 a")

    def arama_yap(self, kelime):
        arama_kutusu = self.driver.find_element(*AramaSayfasi.ARAMA_KUTUSU)
        arama_kutusu.send_keys(kelime)
        arama_kutusu.send_keys(Keys.ENTER)


    def arama_uyari_mesajini_ver(self):
        mesaj = self.driver.find_element(*AramaSayfasi.ARAMA_UYARI_MESAJI).text.strip()
        return mesaj

    def aranan_urun_isimlerini_liste_ver(self):
        urunler = self.webelement_listesinden_string_listesi_ver(AramaSayfasi.ARANAN_URUNLER)
        return urunler