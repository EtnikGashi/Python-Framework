from curses import noecho
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from testBase.web_driver_factory import WebDriverFactory
from selenium.common.exceptions import TimeoutException

class Navigation:
    '''
    Selenium functions modified in a proper way
    '''
    def __init__(self):
        self.driver = WebDriverFactory.get_driver()

    def is_element_available(self, locator,
     element_text: str = None) -> WebElement:
        '''
        Checks if element is available and returns it if available, if not returns None
        '''
        ignore_list = [ NoSuchElementException ]
        wait = WebDriverWait(self.driver, 2, 0.250, ignore_list)
        try:
            element_found = wait.until(IsAvailable(locator, element_text))
        except TimeoutException as no_element:
            raise NoSuchElementException("Couldn't locate element within 10 seconds") from no_element
        return element_found

class IsAvailable:
    '''
    Checks if element is available or not
    '''
    def __init__(self, locator, element_text):
        self.driver = WebDriverFactory.get_driver()
        self.locator = locator
        self.element_text: str = element_text

    def __call__(self, driver):
        try:
            is_displayed = False
            print(self.driver.find_element(*self.locator).text)
            if (self.driver.find_element(*self.locator).is_displayed
            and self.driver.find_element(*self.locator) is not None):
                is_displayed = True

            if is_displayed and self.element_text:
                if self.driver.find_element(*self.locator).text == self.element_text:
                    return self.driver.find_element(*self.locator)
            elif is_displayed:
                return self.driver.find_element(*self.locator)
            else:
                return False
        except Exception:
            return False
