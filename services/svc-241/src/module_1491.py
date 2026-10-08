"""Service module 1491: business logic, no crypto."""


def calculate_total_1491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1491():
    return 'module 1491 handles orders and invoices'
