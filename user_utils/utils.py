import json
import os
from datetime import datetime


def load_data():
    """
    Загружаем json файл
    :return: dict словарь данных по операциям
    """
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


def executed_operation(data_dict):
    """
    Формируем список словарей выполненных операций
    :param data_dict: dict
    :return: list
    """
    executed_list = []
    for item in data_dict:
        if 'state' in item and item['state'] == 'EXECUTED':
            executed_list.append(item)

    return executed_list


executed_state_list = executed_operation(data)


def sorted_by_date(executed_list):
    """
    Сортируем операции по дате и времени исполнения.
    Возвращаем последние 5 операций
    :param executed_list: list
    :return: dict
    """
    for i in executed_list:
        i['date'] = ' '.join(i['date'][:-7].split('T'))

    sorted_dict = sorted(executed_list, key=lambda x: x['date'], reverse=True)

    return sorted_dict[:5]


sorted_dict_list = sorted_by_date(executed_state_list)


def prepare_info_for_print(output_data):
    """
    Форматируем данные словаря в требуемый вид для вывода
    :param output_data: dict
    :return: dict
    """
    for i in output_data:
        format_date = datetime.strptime(i['date'], '%Y-%m-%d %H:%M:%S')
        new_format_date = format_date.strftime('%d.%m.%Y %H:%M:%S')
        i['date'] = new_format_date

        if 'from' in i:
            account_from = i['from'].split()
            i['from'] = account_from
            modify_account = i['from'][len(i['from']) - 1]
            modify_account = (modify_account[:6] + '*' * 6 + modify_account[len(modify_account)-4:])
            modify_account = ' '.join(modify_account[i:i + 4] for i in range(0, len(modify_account), 4))
            i['from'][len(i['from']) - 1] = modify_account
        else:
            i['from'] = '-'

        if 'to' in i:
            account_to = i['to'].split()
            i['to'] = account_to
            i['to'][1] = '**' + i['to'][1][len(i['to'][1])-4:]
        else:
            i['to'] = '-'

    return output_data


modify_operation_dict = prepare_info_for_print(sorted_dict_list)


def print_operation(printed_operation):
    """
    Вывод последних 5-и операций
    :param printed_operation: dict
    :return: None
    """
    for i in printed_operation:
        print(f'{i['date']} {i['description']}')
        print(f'{' '.join(i['from'])} -> {' '.join(i['to'])}')

        print(f'{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}')
        print()


print_operation(modify_operation_dict)
