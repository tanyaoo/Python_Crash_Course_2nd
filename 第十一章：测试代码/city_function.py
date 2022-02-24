def get_formatted_name(city, country, population=''):
    """生成格式化的名称"""
    if population:
        formatted_name = f"{city} {country} - population {population}"
    else:
        formatted_name = f"{city} {country}"
    return formatted_name.title()

# name = get_formatted_name('shanghai', 'china')
# print(name)
