import citesting.citesting as ci

def test_ci_f_0():
    assert ci.f(0) == 0

def test_ci_f_1():
    assert ci.f(1) == 2
    assert ci.f(2) == 6

