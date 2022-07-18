'''
Test steps
'''

import time
import pytest
from qaseio.pytest import qase
from popo.user import User
from test_steps.step_login import StepLogin
from decorators.screenshot import screenshot
from data_providers.user_provider import get_users

@pytest.mark.parametrize("user", get_users())
@qase.id(1)
@screenshot.on_failure
def test_first(user: User):
    '''
    First test
    '''
    step_login = StepLogin()
    step_login.enter_user_name(user.username)
    step_login.enter_password(user.password)
    step_login.click_login_button()
    time.sleep(3)
    step_login.verify_login()

@qase.id(2)
@screenshot.on_failure
@pytest.mark.parametrize("user", get_users())
def test_second(user: User):
    '''
    Second test
    '''
    step_login = StepLogin()
    step_login.enter_user_name(user.username)
    step_login.enter_password(user.password)
    step_login.click_login_button()
    time.sleep(3)
    step_login.verify_login_unsuccessful()
