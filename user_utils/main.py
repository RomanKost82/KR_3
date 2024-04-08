from user_utils.utils import (
    load_data,
    executed_operation,
    sorted_by_date,
    prepare_info_for_print
)


def print_operation(printed_operation):
    """
    Вывод последних 5-и операций
    :param printed_operation: dict
    :return: None
    """
    for i in printed_operation:
        print(f"{i['date']} {i['description']}")
        print(f"{' '.join(i['from'])} -> {' '.join(i['to'])}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()


if __name__ == '__main__':
    data = load_data()
    executed_state_list = executed_operation(data)
    sorted_dict_list = sorted_by_date(executed_state_list)
    modify_operation_dict = prepare_info_for_print(sorted_dict_list)
    print_operation(modify_operation_dict)
