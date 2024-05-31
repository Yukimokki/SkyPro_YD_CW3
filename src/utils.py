import json
def load_json():
    """
    загружает банковский отчет
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations  =  json.load(file)
        return operations

#print(load_json())