import json


def trans_load(num_operations):
    """
    загружает банковский отчет и выбирает 5 последних успешных операции
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        trans_list = [x for x in json.load(file) if x and x["state"] == "EXECUTED"]
        trans_list.sort(key=lambda k: str(k.get('date')), reverse=True)
        return trans_list[0:int(num_operations)]


def trans_dict(operations_list):
    """
   выбирает нужные значения для формирования выписки
   """

    transactions = operations_list
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
    card_number_list = (card_number[:-12:1], " ", card_number[-12:-10:1], "** **** ", card_number[-5:-1:1])
    card_number_format = "".join(card_number_list)
    return card_number_format


def origin_format(origin):
    """
    выбирает функцию форматирования просихождения операции
    """
    if origin and origin[0:4] == 'Счет':
        trans_from = trans_dict_format_acc(origin)
    elif origin and origin[0:4] != 'Счет':
        trans_from = trans_dict_format_card(origin)
    elif origin == None:
        trans_from = 'Нет'
    return trans_from


def dest_format(destination):
    """
    выбирает функцию для форматирования назначения операции
    """
    if destination[0:4] == 'Счет':
        trans_to = trans_dict_format_acc(destination)
    elif destination[0:4] != 'Счет':
        trans_to = trans_dict_format_card(destination)
    return trans_to


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


def trans_printout():
    """
    выполняет печатть необходимого числа транзакций
    * не выполнена
    """
    pass
