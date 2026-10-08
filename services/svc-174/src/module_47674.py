"""Service module 47674: business logic, no crypto."""


def calculate_total_47674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47674():
    return 'module 47674 handles orders and invoices'
