from pprint import pprint
import os


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


text1 = open('1.txt', 'rt', encoding='utf-8')
text2 = open('2.txt', 'rt', encoding='utf-8')
text3 = open('3.txt', 'rt', encoding='utf-8')


if text1 or text2 or text3 is None:
    text1 = '1.txt'
    text2 = '2.txt'
    text3 = '3.txt'
    final_file = "full_file.txt"
    file1_path = os.path.join(os.getcwd(), text1)
    file2_path = os.path.join(os.getcwd(), text2)
    file3_path = os.path.join(os.getcwd(), text3)
    
    with open(file1_path, 'rt', encoding='utf-8') as f1:
            file1 = f1.readlines()
    with open(file2_path, 'rt', encoding='utf-8') as f2:
            file2 = f2.readlines()
    with open(file3_path, 'rt', encoding='utf-8') as f3:
            file3 = f3.readlines()
    with open(final_file, 'w', encoding='utf-8') as f_total:

        if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(text1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(text2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(text3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(text1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                f_total.write(text2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
        elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                f_total.write(text3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(text1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
        elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(text2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
        elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(text3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
        else:
            print('Что-то пошло не так')
 

