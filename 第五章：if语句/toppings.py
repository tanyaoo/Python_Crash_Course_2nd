# request_toppings = ['mushrooms','green peppers','extra cheese']

# for request_topping in request_toppings:
#     if request_topping == 'green peppers':
#         print('Sorry,we are out of green peppers right now.')
#     else:
#         print(f'{request_topping} adding.')
# print('\nFinish making your pizza.')


request_toppings = []

if request_toppings:                                #检查列表是否为空，当不为空时执行下面缩进的语句
    for request_topping in request_toppings:
        print(f'{request_topping} adding.')
    print('\nFinished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')
