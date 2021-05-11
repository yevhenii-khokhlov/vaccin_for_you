from prettytable import PrettyTable


def remake(raw_data: dict):
    values = raw_data.values()
    headers = set()
    for values in values:
        headers.update(values)
    th = sorted(list(headers))
    td = []
    items = raw_data.items()
    for item in items:
        row = []
        for header in th:
            if header in item[1]:
                row.append(item[0])
            else:
                row.append('-')
        td.append(row)

    return th, td


def print_table(raw_data: dict):
    th, td = remake(raw_data)
    table = PrettyTable(th)
    for row in td:
        table.add_row(row=row)
    print(table)
