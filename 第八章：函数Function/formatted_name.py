def built_person(first_name, last_name, age=None):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = built_person('tan', 'yao', 30)
print(musician)


