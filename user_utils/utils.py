import json
import os
from collections import OrderedDict

def load_data():
    # Получаем текущую директорию скрипта
    current_directory = os.path.dirname(__file__)
    # Переходим на один уровень вверх (родительская директория)
    parent_directory = os.path.dirname(current_directory)
    # Формируем путь к файлу operations.json, используя относительный путь к папке data
    json_file_path = os.path.join(parent_directory, 'data', 'operations.json')

    with open(json_file_path, 'r', encoding='UTF-8') as json_file:
        data_operations = json.load(json_file)


    return data_operations


data = load_data()

def executed_operation(data):
    executed_list = []
    for item in data:
        if 'state' in item and item['state'] == 'EXECUTED':
            executed_list.append(item)

    return executed_list


executed_list = executed_operation(data)

print(executed_list)

print(executed_list[1]['state'])

def sorted_by_date(executed_list):
    for i in executed_list:
        i['date'] = i['date'][:-7].split('T')

    sorted_dict = sorted(executed_list, key=lambda x: x['date'], reverse=True)

    return sorted_dict[:5]

sorted_dict = sorted_by_date(executed_list)

print(len(sorted_dict))



# if __name__ == '__main__':
#     print(load_data())
