import json
import os

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
    executed_list = {}
    for i in data:
        if 'state' in i and i['state'] == 'EXECUTED':
            executed_list.update(i)


    print(executed_list)

executed = executed_operation(data)

# def sorted_by_date():


# if __name__ == '__main__':
#     print(load_data())
