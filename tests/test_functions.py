import citesting.citesting as ci
import pytest


def test_ci_f_0():
    '''testing citesting.citesting.f(x) function'''
    assert ci.f(0) == 0


def test_ci_f_1():
    '''testing citesting.citesting.f(x) function'''
    assert ci.f(1) == 2
    assert ci.f(2) == 6


def test_ci_f2_0():
    '''testing citesting.citesting.f2(x) function'''
    assert ci.f2(0) == 0
    assert ci.f2(2) == 4


@pytest.mark.xfail(raises=AssertionError)
def test_ci_f2_1():
    '''testing citesting.citesting.f2(x) function'''
    assert ci.f2(3) != 10  # raises AssertionError