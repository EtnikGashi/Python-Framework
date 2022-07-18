from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverFactory:
    '''This class is used to handle driver'''
    driver: webdriver.Chrome = None
    @staticmethod
    def get_driver():
        '''If driver object is initiated it will return it
            If not it will create a new one'''
        try:
            if WebDriverFactory.driver is None:
                service = Service(ChromeDriverManager().install())
                WebDriverFactory.driver = webdriver.Chrome(service=service)
        except Exception as exception:
            raise Exception("Driver instatiation error:"+ exception.with_traceback) from exception
        return WebDriverFactory.driver

    @staticmethod
    def quit():
        '''If driver object is initiated it will quit it'''
        if WebDriverFactory.driver is not None:
            WebDriverFactory.driver.quit()
