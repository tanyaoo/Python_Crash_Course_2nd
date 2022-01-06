while True:
    age = input('How old are you:')
    age = int(age)
    if age < 3 and age > 0:
        print('It`s free for you!')
    elif age >=3 and age <= 12:
        print('Your fare is $10.')
    elif age > 12 and age < 100:
        print('Your fare is $15.')
    elif age <= 0 or age >= 100:
        break    
    


