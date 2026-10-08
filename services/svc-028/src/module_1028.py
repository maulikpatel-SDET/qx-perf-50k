"""Service module 1028: business logic, no crypto."""


def calculate_total_1028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1028():
    return 'module 1028 handles orders and invoices'
