from selenium.webdriver.common.by import By

class HomePage:
    '''
    Home page
    '''
    def __init__(self):
        self.user_name = (By.ID, 'users-name')