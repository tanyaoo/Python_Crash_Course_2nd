person_1 = {
    'name':'tanyao',
    'age':30,
    'city':'xuanen',
    }

person_2 = {
    'name':'cml',
    'age':30,
    'city':'wanzhai',
    }

person_3 = {
    'name':'musk',
    'age':45,
    'city':'los'
    }

people = [person_1,person_2,person_3]

for person in people:
    for key,value in person.items():
        message = f'The person`s {key} is {value}.'
        print(message)
    print()

