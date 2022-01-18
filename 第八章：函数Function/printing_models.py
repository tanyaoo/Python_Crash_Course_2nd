# unprinting_models = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinting_models:
#     current_model = unprinting_models.pop()
#     print(f'Printing_model:{current_model}')
#     completed_models.append(current_model)
#
#
# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)


def printing_modle(unprinting_models,completed_models):
    """打印每一个设计"""
    while unprinting_models:
        current_model = unprinting_models.pop()
        print(f'Printing model:{current_model}')
        completed_models.append(current_model)


def show_completed_models(completed_models):
    """显示打印好的模型"""
    for completed_model in completed_models:
        print(f'-{completed_model}')


unprinting_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_modle(unprinting_models, completed_models)
print('\nThe following models have been printed:')
show_completed_models(completed_models)

