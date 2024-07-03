import pytest

# In this the setup  will run for every individual test both before yeild and after yield that is
# written in the conftest.py file
@pytest.mark.usefixtures("setup")
class TestExample():
    def test_fixtureDemo1(self):
        print("I'm demo1")

    def test_fixtureDemo2(self):
        print("I'm demo2")

    def test_fixtureDemo3(self):
        print("I'm demo3")

    def test_fixtureDemo4(self):
        print("I'm demo4")