def make_pizza(size, *toppings):
    """形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将
    收到的所有值都封装到这个元组中。
    打印顾客点的所有配料"""
    print(f'\n{toppings}')         # 证明toppings确实是一个元组，并且封装了所有接收到的值
    print(f'Make a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')


make_pizza(3, 'peperoni', 'tan8yao')
make_pizza(6, 'mushrooms', 'peperoni', 'tanyao')

