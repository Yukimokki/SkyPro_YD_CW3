from utils import *

def main():
    num_operations = 5
    operations = trans_dict(trans_load(num_operations))

    for operation in operations:
        date = trans_dict_format_date(operation["date"])
        trans_from = origin_format(operation['from'])
        trans_to = dest_format(operation['to'])

        print(f"""
        {date} {operation['description']}
        {trans_from} -> {trans_to}
        {operation['summ']} {operation['currency']}""")

#main()