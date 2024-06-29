import pytest


@pytest.mark.smoke
def test_Greet():
    msg = "Hello"
    assert msg == "Hi", "There is no match"

def test_SumMath():
    a=6
    b=4
    assert a+b == 10, "Sum is not a match #BadMath"