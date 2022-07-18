import json
from typing import List
from popo.user import User

def get_users():
    file = open('test_data/login.json')
    users_json = json.load(file)
    users_list = [*users_json]

    for user in users_list:
        yield User(**user['users'])
    