import json
from datetime import datetime

def read_operations():
    """Функция считывает данные из JSON-файла и преобразует"""
    with open('operations.json', 'r') as file:
        operations = json.load(file)
    return operations

def filter_operations(operations, status):
    """Функция фильтрует операции по статусу"""
    filtered_operations = filter(lambda operation: 'state' in operation and operation['state'] == status, operations)
    return list(filtered_operations)

def sort_operations(operations):
    """Функция сортирует операции по дате"""
    sorted_operations = sorted(operations, key=lambda operation: datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sorted_operations

def get_last_operations(operations):
    """Функция делает срез 5 последних операций"""
    last_operations = operations[:5]
    return last_operations

def mask_card_number(card_number):
    """Функция маскирует карту"""
    words = card_number.split()
    last_word = words[-1]

    replaced_word = last_word[:4] + ' ' + last_word[4:6] + '** ' + '**** ' + last_word[12:]

    words[-1] = replaced_word
    result = ' '.join(words)
    return result


def mask_account_number(account_number):
    """Функция маскирует номер счета"""
    masked_account_number = f'Счет **{account_number[-4:]}'
    return masked_account_number

def print_operation(operation):
    """Функция вывода"""
    date = datetime.strptime(operation.get('date'), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
    description = operation.get('description')
    from_account = operation.get('from')
    to_account = operation.get('to')
    amount = operation.get('operationAmount', {}).get('amount')
    currency = operation.get('operationAmount', {}).get('currency', {}).get("code")

    if from_account is None:
        from_account = ""
    elif "Счет" in from_account:
        from_account = mask_account_number(from_account)
    else:
        from_account = mask_card_number(from_account)

    if to_account is None:
        to_account = ""
    elif "Счет" in to_account:
        to_account = mask_account_number(to_account)
    else:
        to_account = mask_card_number(to_account)

    print(f'{date} {description}')
    print(f'{from_account} -> {to_account}')
    print(f'{amount} {currency}\n')

def main():
    operations = read_operations()
    executed_operations = filter_operations(operations, 'EXECUTED')
    sorted_operations = sort_operations(executed_operations)
    last_operations = get_last_operations(sorted_operations)
    for operation in last_operations:
        print_operation(operation)

if __name__ == '__main__':
    main()
