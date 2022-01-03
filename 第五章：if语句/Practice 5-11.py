numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(f'{number}序数为{number}st.')
    elif number == 2:
        print(f'{number}序数为{number}nd.')
    elif number == 3:
        print(f'{number}序数为{number}rd.')
    else:
        print(f'{number}序数为{number}th.')
