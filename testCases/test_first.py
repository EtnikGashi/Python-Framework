import time
from main.navigation import Navigation
from pages.home_page import HomePage

def test_first():
    nav = Navigation()
    # element.send_keys('Hello')
    home = HomePage()
    element = nav.is_element_available(home.user_name)
    element.send_keys('hello')
    time.sleep(2)