"""Service module 47490: business logic, no crypto."""


def calculate_total_47490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47490():
    return 'module 47490 handles orders and invoices'
