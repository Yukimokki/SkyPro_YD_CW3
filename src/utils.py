import json
import os


def trans_load(filepath):
    """
    загружает банковский отчет и выбирает 5 последних успешных операции
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        trans_list_raw = json.load(file)
    return trans_list_raw


def trans_filter(trans_list_raw, status):
    """
    фильтрует успешные операции
    """
    trans_list_filt = [x for x in trans_list_raw if x and x["state"] == status]
    return trans_list_filt


def trans_sort(trans_list_filt,sorted):
    """
    сортирует по датам и выбирает 5 последних операций
    """
    trans_list_filt.sort(key=lambda k: str(k.get(sorted)), reverse=True)
    #trans_list_sort = trans_list_filt[0:int(num_operations)]
    return trans_list_filt


def trans_dict(trans_list_sort):
    """
   выбирает нужные значения для формирования выписки
   """

    transactions = trans_list_sort
    trans_list_items = []
    for trans in transactions:
        transaction = {"state": trans["state"], "date": trans["date"], "description": trans['description'],
                       "from": trans.get("from"), "to": trans["to"], "summ": trans["operationAmount"]["amount"],
                       "currency": trans["operationAmount"]["currency"]["name"], "id": trans['id']}
        trans_list_items.append(transaction)

    return trans_list_items


def trans_dict_format_card(card_number):
    """
    форматирует номер карты
    """
    card_number_list = (card_number[:-12:1], " ", card_number[-12:-10:1], "** **** ", card_number[-4::1])
    card_number_format = "".join(card_number_list)
    return card_number_format


def hide_requisites(origin):
    """
    выбирает функцию форматирования просихождения операции
    """
    if not origin:
        return "Нет"
    if origin.lower().startswith('счет'):
        hidden_requisites = trans_dict_format_acc(origin)
    else:
        hidden_requisites = trans_dict_format_card(origin)

    return hidden_requisites


def trans_dict_format_acc(account):
    """
    форматирует значения номера счёта
    """
    return 'Счет **' + account[-4:]


def trans_dict_format_date(trans_date):
    """
    выводит правильный формат даты
    """
    date = trans_date.split('T')
    date_items = date[0].split('-')
    date_list = [date_items[2], date_items[1], date_items[0]]
    date_format = ".".join(date_list)
    return date_format
