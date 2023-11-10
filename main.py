# Задание 1

import os

path = os.path.join(os.getcwd(), 'Text.txt')
with open(path) as Text_file:
    cook_book = {}
    for string in Text_file:
        dish = string.strip()
        ingredients_count = int(Text_file.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredients_name, quantity, measure = Text_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredients_name,
                              'quantity': quantity,
                              'measure': measure})
        cook_book[dish] = dish_dict
        Text_file.readline()


#  Задание 2
# noinspection PyUnreachableCode
def cook_list(dishes, person_count):
    cook_list = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            ingredients_list = dict([(ingredient['ingredient_name'],
                                      {'quantity': int(ingredient['quantity']) * person_count,
                                       'measure': ingredient['measure']})])
            if cook_list.get(ingredient['ingredient_name']) == 'None':
                union = (int(cook_list[ingredient['ingredient_name']]['quantity']) +
                         int(ingredients_list[ingredient['ingredient_name']]['quantity']))
                cook_list[ingredient['ingredient_name']]['quantity'] = union
            else:
                cook_list.update(ingredients_list)
    return cook_list

    print (cook_list({'Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'}, 5))
