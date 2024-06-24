import pytest

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b

def bolme(a,b):
    return a/b
def carpma(a,b):
    return a*b

@pytest.mark.skip
def test_toplama():
    assert 4 == toplama(2,2)

@pytest.mark.xfail
def test_cikarma():
    assert 3 == cikarma(5,3)

def test_bolme():
    assert 5== bolme(15,3)

def test_carpma():
    assert 10== carpma(2,5)



