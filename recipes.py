from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        ingredient_name = line.strip()
        amount = int(file.readline().strip())
        recipes = []
        for _ in range(amount):
            ingridient, quantity, unit_of_measurement = file.readline().strip().split(' | ')
            recipes.append({
                'ingridient': ingridient,
                'quantity': int(quantity),
                'unit_of_measurement': unit_of_measurement
            })
            
        file.readline()
        cook_book[ingredient_name] = recipes

pprint(cook_book, sort_dicts = False)

def get_shop_list_by_dishes(dishes, person_count):
    ingridient_list = dict()
    for dish_name in dishes:  
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  
                meas_quan_list = dict()
                if ings['ingridient'] not in ingridient_list:
                    meas_quan_list['unit_of_measurement'] = ings['unit_of_measurement']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingridient_list[ings['ingridient']] = meas_quan_list
                else:
                    ingridient_list[ings['ingridient']]['quantity'] = ingridient_list[ings['ingridient']]['quantity'] + ings['quantity'] * person_count  
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingridient_list

    
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))