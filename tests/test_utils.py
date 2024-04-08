import pytest
from datetime import datetime
from user_utils.utils import load_data, executed_operation, sorted_by_date, prepare_info_for_print, print_operation


@pytest.fixture(scope="module")
def data():
    return load_data()


def test_load_data(data):
    assert isinstance(data, dict)
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
    output_data = [
        {'date': '2020-10-16T14:20:00', 'from': '1234567890123456', 'to': '9876543210987654', 'description': 'Payment',
         'operationAmount': {'amount': '100.00', 'currency': {'name': 'USD'}}}
    ]
    modified_data = prepare_info_for_print(output_data)
    assert isinstance(modified_data, list)
    assert len(modified_data) == 1
    item = modified_data[0]
    assert 'date' in item
    assert isinstance(datetime.strptime(item['date'], '%d.%m.%Y %H:%M:%S'), datetime)
    assert 'from' in item
    assert item['from'] == '1234************3456'
    assert 'to' in item
    assert item['to'] == '98**6543210987654'
    assert 'description' in item
    assert 'operationAmount' in item
    assert isinstance(item['operationAmount'], dict)


def test_print_operation(capsys):
    printed_operation = [
        {'date': '16.10.2020 14:20:00', 'from': '1234567890123456', 'to': '9876543210987654', 'description': 'Payment',
         'operationAmount': {'amount': '100.00', 'currency': {'name': 'USD'}}}
    ]
    print_operation(printed_operation)
    captured = capsys.readouterr()
    assert '16.10.2020 14:20:00 Payment\n' in captured.out
    assert '1234************3456 -> 98**6543210987654\n' in captured.out
    assert '100.00 USD\n\n' in captured.out


if __name__ == '__main__':
    pytest.main()
