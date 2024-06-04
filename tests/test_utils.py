from src.utils import *
import os

def test_load():
    TEST_DATA_PATH = os.path.join(os.path.dirname(__file__),'test_operations.json')
    assert trans_load(TEST_DATA_PATH) == [{"state": "executed", "date": "15.11.2024"},{"state": "executed", "date": "10.10.2024"}, {"state": "canceled", "date": "15.11.2022"}]

def test_filt():
    assert trans_filter([{"state": "executed", "date": "15.11.2024"},{"state": "executed", "date": "10.10.2024"}, {"state": "canceled", "date": "15.11.2022"}], 'executed') == \
           [{"state": "executed", "date": "15.11.2024"}, {"state": "executed", "date": "10.10.2024"},]


def test_sort():
    assert trans_sort([{"state": "executed", "date": "15.11.2024"}, {"state": "executed", "date": "10.10.2024"}], 'date') == \
            [{"state": "executed", "date": "15.11.2024"}, {"state": "executed", "date": "10.10.2024"}]

def test_date():
    assert trans_dict_format_date('2019-12-08T22:46:21.935582') == '08.12.2019'

def test_acc():
    assert trans_dict_format_acc('Счет 90424923579946435907') == 'Счет **5907'

def test_card():
    assert trans_dict_format_card('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'

def test_hide_requisites():
    assert hide_requisites('') == 'Нет'
    assert hide_requisites('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert hide_requisites('Счет 90424923579946435907') == 'Счет **5907'

