import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """获取新用户"""
    username = input("what is your name :")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """欢迎回来，并指出用户的名字"""
    username = get_stored_username()
    if username:
        your_name = input("what is your name:")
        if username == your_name:
            print(f"welcome back, {username}")
        else:
            your_name = get_new_username()
            print("we will remember you when you come back.")
    else:
        username = get_new_username()
        print(f"we will remember you when you come back, {username} !")


greet_user()
