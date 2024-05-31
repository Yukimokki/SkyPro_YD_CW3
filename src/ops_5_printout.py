from src.utils import load_json

def main():
    operations = load_json()
    counter = 0
    for operation in operations:
        while counter < 5:
            if operation["state"] == "EXECUTED":
                counter += 1

                date_list = (operation["date"][8:10],operation["date"][5:7],operation["date"][0:4])
                date = ".".join(date_list)
                op_description = operation["description"]
                if operation["from"][0:4] == "Счет":
                    origin_list = (operation["from"][0:5], " **",operation["from"][-5:-1:1])
                    origin = "".join(origin_list)
                elif operation["from"][0:4] != "Счет":
                    origin_list = (operation["from"][:-12:1], " ", operation["to"][-12:-10:1], "** **** ", operation["from"][-5:-1:1] )
                    origin = "".join(origin_list)
                if operation["to"][0:4] == "Счет":
                    destination_list = (operation["to"][0:5], " **", operation["to"][-5:-1:1])
                    destination = "".join(destination_list)
                elif operation["to"][0:4] != "Счет":
                    destination_list = (operation["to"][:-12:1], " ", operation["to"][-12:-10:1], "** **** ", operation["to"][-5:-1:1] )
                    destination = "карта"
                summ = operation["operationAmount"]["amount"]
                currency = operation["operationAmount"]["currency"]["name"]

                report = {"date":date, "operation":op_description, "from":origin,"destination": destination, "summ": summ, "currency":currency}
                #print(report)

                print(f"""
                {date} {op_description}
                {origin} -> {destination}
                {summ} {currency}""")


main()



# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.