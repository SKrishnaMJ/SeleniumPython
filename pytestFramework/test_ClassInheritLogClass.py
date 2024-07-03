import pytest

from pytestFramework.LogClass import LogClass

@pytest.mark.usefixtures("setup1")
class TestLogInheritance(LogClass):
    def test_LogDemo1(self):
        log = self.getLogger()
        log.info("This is a inherited logclass demo1")

    def test_LogDemo2(self):
        log = self.getLogger()
        log.info("This is a inherited logclass demo2")



