from src.utils import *


def test_load():
    assert len(trans_load(5)) == 5

def test_date():
    assert trans_dict_format_date('2019-12-08T22:46:21.935582') == '08.12.2019'

def test_acc():
    assert trans_dict_format_acc('Счет 90424923579946435907') == 'Счет **5907'

def test_card():
    assert trans_dict_format_card('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'

def test_origin():
    assert origin_format(None) == 'Нет'
    assert origin_format('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert origin_format('Счет 90424923579946435907') == 'Счет **5907'


def test_destination():
    assert dest_format('Visa Classic 2842878893689012') == 'Visa Classic 2842 87** **** 9012'
    assert dest_format('Счет 90424923579946435907') == 'Счет **5907'
