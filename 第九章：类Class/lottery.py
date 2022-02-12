from random import choice

number_pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')
prize_number = [0, 8, 2, 6, 'c', 'e']

quality = 0
while True:
    get_number = []
    for x in range(6):
        number = choice(number_pool)
        get_number.append(number)
    quality += 1
    if get_number == prize_number:
        print("恭喜你，中大奖了！！！")
        break
    else:
        print(quality)

