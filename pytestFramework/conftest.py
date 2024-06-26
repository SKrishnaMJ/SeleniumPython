import pytest

# This is how a fixture is defined using @pytest.fixture()

# The first fixture runs every step for every test
@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I'm last")

# When the scope is defined that means it runs at the beginning of the class and the yeild runs after
# all the tests in the class are done executing
@pytest.fixture(scope="class")
def setup1():
    print("I will be executing first as setup1")
    yield
    print("I'm last as setup2")

@pytest.fixture()
def dataLoad():
    print("Data is coming from this fixture")
    return ["Sai", "Krishna", "Hazard"]

@pytest.fixture(params=[("Yeah", "Boi"), "Sai"])
def paramFixture(request):
    print("Paramters coming from fixtures")
    return request.param