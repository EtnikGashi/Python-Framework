from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from test_base.web_driver_factory import WebDriverFactory

class Navigation:
    '''
    Selenium navigations
    '''
    def __init__(self):
        self.driver = WebDriverFactory.get_driver()

    def is_element_available(self, locator,
     element_text: str = None) -> WebElement:
        '''
        Checks if element is available and returns it if available, if not returns None
        '''
        ignore_list = [ NoSuchElementException ]
        wait = WebDriverWait(self.driver, 10, 0.250, ignore_list)
        try:
            element_found = wait.until(is_available(locator, element_text))
        except TimeoutException as no_element:
            raise NoSuchElementException(
                "Couldn't locate element within 10 seconds"
                ) from no_element
        return element_found

    def send_keys_to_element(self, locator, text):
        '''
        Used to send keys to an element
        '''
        element_to_send_keys_to = Navigation.is_element_available(self, locator)

        try:
            element_to_send_keys_to.send_keys(text)
        except Exception as send_keys_exception:
            raise Exception(
                "There was an error trying to send keys"
                ) from send_keys_exception


    def click_element(self, locator):
        '''
        Used to click an element.
        '''
        element_to_be_clicked = Navigation.is_element_available(self, locator)

        try:
            element_to_be_clicked.click()
        except Exception as click_exception:
            raise Exception(
                "There was an error trying to click an element"
            ) from click_exception


def is_available(locator, element_text):
    '''
    Checks whether an  element is available or not
    '''
    def _predicate(driver):
        try:
            is_displayed = False
            if (driver.find_element(*locator).is_displayed
            and driver.find_element(*locator) is not None):
                is_displayed = True

            if is_displayed and element_text:
                if driver.find_element(*locator).text == element_text:
                    return driver.find_element(*locator)
            elif is_displayed:
                return driver.find_element(*locator)
            else:
                return False
        except Exception: #pylint: disable=broad-except
            return False
    return _predicate
