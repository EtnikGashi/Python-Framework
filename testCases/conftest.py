import pytest
from testBase.web_driver_factory import WebDriverFactory

@pytest.fixture(autouse=True)
def setup_and_tear_down():
    '''
    Everything that happens before and after a test is run
    '''
    WebDriverFactory.get_driver().get("https://www.saucedemo.com/")

    yield

    WebDriverFactory.quit()
