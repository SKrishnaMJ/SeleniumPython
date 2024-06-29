import pytest

@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I'm last")


@pytest.mark.smoke
def test_fixtureTestDemo(setup):
    print("This is the test")