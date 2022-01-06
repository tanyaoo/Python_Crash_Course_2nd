#披萨配料
active = True
while active:
    ingredients = input('please enter a kind of ingredient:')
    if ingredients == 'quit':
        active = False
    else:
        print(f'We will add {ingredients} in the pizza.')
