cities = {
    'shanghai':{
        'country':'china',
        'population':100000,
        'fact':'中国最大的城市',
    },
    'beijing':{
        'country':'china',
        'population':20000,
        'fact':'首都',
    },
    'enshi':{
        'country':'china',
        'population':1000,
        'fact':'小城市',
    },

    }

for city ,message in cities.items():
    print(f'\ncity:{city}')
    print(f'country:{message["country"]}')
    print(f'population:{message["population"]}')
    print(f'fact:{message["fact"]}')
        
