import pytest


def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a == b, "Test failed as a is not equal to b."


@pytest.mark.login
def test_m2():
    name = "Selenium"
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


def test_login_two():
    assert "admin" == "admin"
