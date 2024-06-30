import pytest

# Make sure the class name also starts with the word Test
# We pass dataLoad fixture as a parameter to the function even though we have defined it before the class
# because we are driving data from this fixture and hence we pass as a parameter

@pytest.mark.usefixtures("dataLoad")
class TestData:
    def test_dynamicData(self, dataLoad):
        for i in dataLoad:
            print(i)