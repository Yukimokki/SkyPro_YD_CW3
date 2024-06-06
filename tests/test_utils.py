from src.utils import trans_load, trans_filter, trans_sort, trans_dict_format_date,\
    trans_hide_account, trans_hide_card_number, hide_requisites
import os

#TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), 'test_operations.json')

def test_load():
    TEST_DATA_PATH = os.path.join(os.path.dirname(__file__),'test_operations.json')
    assert trans_load(TEST_DATA_PATH) == [
        {"state": "executed", "date": "2024-11-15"},
        {"state": "executed", "date": "2024-10-10"},
        {"state": "canceled", "date": "2022-11-15"}
    ]


def test_filt():
    data = [
        {"state": "executed", "date": "2024-11-15"},
        {"state": "executed", "date": "2024-10-10"},
        {"state": "canceled", "date": "2022-11-15"}
    ]

    expected = [
        {"state": "executed", "date": "2024-11-15"},
        {"state": "executed", "date": "2024-10-10"}
    ]

    assert trans_filter(data, 'executed') == expected


def test_sort():
    data = [
        {"state": "executed", "date": "2024-11-15"},
        {"state": "executed", "date": "2024-10-10"}
    ]
    expected = [
        {"state": "executed", "date": "2024-11-15"},
        {"state": "executed", "date": "2024-10-10"}
    ]
    assert trans_sort(data, 'date') == expected

def test_date():
    assert trans_dict_format_date('2019-12-08T22:46:21.935582') == '08.12.2019'

def test_acc():
    assert trans_hide_account('Счет 90424923579946435907') == 'Счет **5907'

def test_card():
    assert trans_hide_card_number('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'

def test_hide_requisites():
    assert hide_requisites('') == 'Нет'
    assert hide_requisites('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert hide_requisites('Счет 90424923579946435907') == 'Счет **5907'

