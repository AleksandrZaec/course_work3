from utils import read_operations, filter_operations, sort_operations, get_last_operations, print_operation


def main():
    operations = read_operations()
    executed_operations = filter_operations(operations, 'EXECUTED')
    sorted_operations = sort_operations(executed_operations)
    last_operations = get_last_operations(sorted_operations)

    for operation in last_operations:
        print_operation(operation)


if __name__ == '__main__':
    main()
