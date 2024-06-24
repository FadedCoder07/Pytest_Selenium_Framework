import pytest
sistem="dev"
def cevre_hesaplama(a,b,c):
    return a+b+c

def alan_hesaplama(taban,yükseklik):
    print("deneme")
    return (taban * yükseklik)/2

@pytest.mark.skip(reason="form css degisti")
def test_ucgen_cevre():
    assert cevre_hesaplama(2,3,3) == 8


@pytest.mark.skipif(sistem=="qa",reason="qa kodu hatalı")
def test_ucgen_alan():
    assert alan_hesaplama(4,3)==6


