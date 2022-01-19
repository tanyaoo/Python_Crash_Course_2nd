def user_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


my_info = user_profile('tan', 'yao',
                       age=30,
                       filed='computer',
                       company='chinamobile')
print(my_info)

