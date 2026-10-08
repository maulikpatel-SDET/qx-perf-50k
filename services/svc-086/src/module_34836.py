"""Service module 34836: business logic, no crypto."""


def calculate_total_34836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34836():
    return 'module 34836 handles orders and invoices'
