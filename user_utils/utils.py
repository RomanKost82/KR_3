import json
import os
from datetime import datetime

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


executed_state_list = executed_operation(data)

print(executed_state_list)

print(executed_state_list[1]['state'])


def sorted_by_date(executed_list):
    for i in executed_list:
        i['date'] = ' '.join(i['date'][:-7].split('T'))

    sorted_dict = sorted(executed_list, key=lambda x: x['date'], reverse=True)

    return sorted_dict[:5]


sorted_dict_list = sorted_by_date(executed_state_list)

print(sorted_dict_list)

print(len(sorted_dict_list))

def prepare_info_for_print(sorted_dict_list):
    for i in sorted_dict_list:
        format_date = datetime.strptime(i['date'], '%Y-%m-%d %H:%M:%S')
        new_format_date = format_date.strftime('%d.%m.%Y %H:%M:%S')
        i['date'] = new_format_date
        print(new_format_date)

        if 'from' in i:
            account_from = i['from'].split()
            i['from'] = account_from
            modify_account = i['from'][len(i['from']) - 1]
            modify_account = (modify_account[:6] + '*' * 6 + modify_account[len(modify_account)-4:])
            modify_account = ' '.join(modify_account[i:i + 4] for i in range(0, len(modify_account), 4))
            print(modify_account)
        else:
            i['from'] = 'Данные отпровителя отсутствуют'

        if 'to' in i:
            account_to = i['to'].split()
            i['to'] = account_to
            i['to'][1] = '**' + i['to'][1][len(i['to'][1])-4:]
            print(account_to)
        else:
            i['to'] = 'Данные получателя отсутствуют'


    print(sorted_dict_list)

prepare_info_for_print(sorted_dict_list)


