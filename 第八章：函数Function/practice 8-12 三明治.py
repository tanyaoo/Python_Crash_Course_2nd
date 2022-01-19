def sandwich_toppings(*toppings):
    print(f'\nMake a sandwich with the following toppings:')
    for topping in toppings:
        print(topping)


sandwich_toppings('11')
sandwich_toppings('111', '222')
sandwich_toppings('111', '222', '333')

