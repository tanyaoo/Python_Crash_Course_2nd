while True:
    message = input('How many people do you have for a dinner?')
    message = int(message)
    if message > 8:
        print('I am sorry,there is not a usefull desk.')
    elif message == 0:
        break
    else:
        print('There is a usefull desk.')
