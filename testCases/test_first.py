'''
Test steps
'''

from qaseio.pytest import qase
from testSteps.step_login import StepLogin

@qase.id(1)
def test_first():
    '''
    First test
    '''
    step_login = StepLogin()
    step_login.enter_user_name("standard_user")
    step_login.enter_password("secret_sauce")
    step_login.click_login_button()
    step_login.verify_login()