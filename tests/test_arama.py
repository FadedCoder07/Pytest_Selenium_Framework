import unittest

import pytest
from ddt import ddt, data, unpack

from Pages.arama_sayfasi import AramaSayfasi
#from utilities.ExcelYardimcisi import ExcelYardimcisi


@pytest.mark.usefixtures("setup")
@ddt
class TestArama(unittest.TestCase):

    # Bu örnekteki gibi veriyi elle yazmak iyi uygulama değil.
    # Bunun yerine aşağıdaki gibi excelden veriyi almak daha doğru
    @data(("ab", "Search term minimum length is 3 characters"), ("abc", "No products were found that matched your criteria."))
    @unpack
    def test_arama_uyari_verir(self, kelime, beklenen_mesaj):
        arama = AramaSayfasi(self.driver)
        arama.arama_yap(kelime)
        mesaj = arama.arama_uyari_mesajini_ver()
        assert mesaj == beklenen_mesaj
