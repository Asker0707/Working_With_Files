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

