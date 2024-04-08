import pytest
from datetime import datetime
from user_utils.utils import executed_operation, sorted_by_date, prepare_info_for_print


@pytest.fixture(scope="module")
def data():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
    ]


def test_load_data(data):
    assert isinstance(data, list)
    assert len(data) > 0


def test_executed_operation(data):
    executed_list = executed_operation(data)
    assert isinstance(executed_list, list)
    for item in executed_list:
        assert item['state'] == 'EXECUTED'


def test_sorted_by_date(data):
    executed_list = executed_operation(data)
    sorted_dict_list = sorted_by_date(executed_list)
    assert isinstance(sorted_dict_list, list)
    assert len(sorted_dict_list) <= 5
    for item in sorted_dict_list:
        assert isinstance(item, dict)
        assert 'date' in item
        assert isinstance(datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S'), datetime)


def test_prepare_info_for_print():
    data = [
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08 22:46:21',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
        {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07 06:17:14',
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'},
    ]
    formatted_data = prepare_info_for_print(data)
    assert len(formatted_data) == 2
    assert formatted_data[0]['date'] == '08.12.2019 22:46:21'
    assert formatted_data[0]['from'] == '-'
    assert formatted_data[1]['to'] == ['Счет', '**3655']


if __name__ == '__main__':
    pytest.main()
