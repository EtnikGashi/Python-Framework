import pytest
from test_base.web_driver_factory import WebDriverFactory

@pytest.fixture(autouse=True)
def setup_and_tear_down():
    '''
    Everything that happens before and after a test is run
    '''
    driver = WebDriverFactory.get_driver()
    driver.get("https://www.saucedemo.com/")

    yield

    driver.quit()