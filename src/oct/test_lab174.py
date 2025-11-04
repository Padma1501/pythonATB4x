import pytest
import allure

@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0

@pytest.mark.smoke
def test_sub1():
    assert 5 - 2 == 3

@pytest.mark.smoke
def test_sub2():
    assert 2 - 1 == 0

@pytest.mark.reg
def test_sub2():
    assert 3 - 1 == 2