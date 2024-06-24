import pytest


def cevre_hesap(a,b,c):
    return a+b+c

def alan_hesap(taban,yükseklik):
    print("deneme")
    return (taban * yükseklik)/2
@pytest.fixture()
def ucgen():
    print("ucgen olusturuldu")
    yield
    print("ucgen yokedildi")
def test_ucgen_cevresi(ucgen):
    assert cevre_hesap(2,3,3) == 8


def test_ucgen_alanı(ucgen):
    assert alan_hesap(4,3)==6