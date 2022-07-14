from qaseio.pytest import qase
from main.navigation import Navigation
from pages.home_page import HomePage

class StepLogin:
    '''
    Steps
    '''
    @qase.step("Enter user name")
    def enter_user_name(self, user_name):
        '''
        Step: Enter user name on login page
        '''
        nav = Navigation()
        home = HomePage()
        nav.send_keys_to_element(home.user_name_input, user_name)


    @qase.step("Enter password")
    def enter_password(self, password):
        '''
        Step: Enter password on login page
        '''
        nav = Navigation()
        home = HomePage()
        nav.send_keys_to_element(home.password_input, password)

    @qase.step("Click Login")
    def click_login_button(self):
        '''
        Step: Click Login button on login page
        '''
        nav = Navigation()
        home = HomePage()
        nav.click_element(home.login_button)

    @qase.step("Verify that the login is successful")
    def verify_login(self):
        '''
        Step: Verify that the login is successful
        '''
        nav = Navigation()
        home = HomePage()
        assert nav.is_element_available(home.title_text) is not None
        