favorite_number = {
    'tanyao':1,
    'cml':2,
    'musk':3,
    'kobe':4,
    'zhi':5
}

message = f'tanyao`s favorite number is {favorite_number["tanyao"]}'
print(message)

#遍历列表方式打印字典信息
# for key,value in favorite_number.items():
#     message = f"{key}`s favorite number is {value}"
#     print(message)