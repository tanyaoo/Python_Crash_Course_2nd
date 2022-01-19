def build_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info     # 返回一个名字为user_info的字典和一个名为name的元组


user_profile = build_profile('tan', 'yao',
                             location='xuanen',     # 等号左边的键没有引号，右边的值有引号，等号两边没有空格
                             age=30,
                             filed='computer')
print(user_profile)
