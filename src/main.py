import os
from utils import trans_load, trans_dict, trans_dict_format_date, \
    trans_filter, trans_sort, hide_requisites

OPERATIONS_PATH = os.path.join(os.path.dirname(__file__), 'operations.json')

def main():
    num_operations = 5
    status = 'EXECUTED'
    sort_on = 'date'

    raw_operations = trans_load(OPERATIONS_PATH)
    filtered_operations = trans_filter(raw_operations, status)
    sorted_operations = trans_sort(filtered_operations, sort_on)
    selected_operations = sorted_operations[0:int(num_operations)]
    operations_formed = trans_dict(selected_operations)


    for operation in operations_formed:
        date = trans_dict_format_date(operation["date"])
        trans_from = hide_requisites(operation['from'])
        trans_to = hide_requisites(operation['to'])

        print(f"""
        {operation['state']}
        {date} {operation['description']}
        {trans_from} -> {trans_to}
        {operation['summ']} {operation['currency']}""")

if __name__ == '__main__':
    main()