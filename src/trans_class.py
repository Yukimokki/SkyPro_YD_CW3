import json
class Transaction:
    def trans_load(self):
        """
        загружает банковский отчет
        """
        with open('operations.json', 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            return transactions
    @property
    def trans_dict(self):
        """
        выбирает нужные значения для формирования выписки
        """
        transactions = self.trans_load()
        for trans in transactions:
            transaction = {"state":trans["state"], "date":trans["date"], "description":trans['description'],
                           "from":trans["from"], "to":trans["to"], "summ":trans["operationAmount"]["amount"],
                           "currency":trans["operationAmount"]["currency"]["name"]}

            return transaction
        #print(transaction)

    def trans_dict_format(self):
        """
        форматирует значения номера карты и счёта
        """
        pass

    def trans_printout(self):
        """
        выполняет печатть необходимого числа транзакций
        """

trans1 = Transaction()
#print(trans1.trans_load())
print(trans1.trans_dict)