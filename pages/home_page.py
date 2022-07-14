'''
Home page module
'''
from selenium.webdriver.common.by import By

class HomePage:
    '''
    Home page
    '''
    def __init__(self):
        self.user_name_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.title_text = (By.XPATH, "//span[@class='title' and .='Products']")
        