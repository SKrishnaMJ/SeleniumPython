import pytest

# In this the setup before yield will run at the beginning once and after every test is completed
# the steps after yeild will run (this is done by defining scope="class" in the ficture method in
# conftest.py file
@pytest.mark.usefixtures("setup1")
class TestExampleNew:
    def test_fixtureDemo10(self):
        print("I'm demo10")

    def test_fixtureDemo20(self):
        print("I'm demo20")

    def test_fixtureDemo30(self):
        print("I'm demo30")

    def test_fixtureDemo40(self):
        print("I'm demo40")