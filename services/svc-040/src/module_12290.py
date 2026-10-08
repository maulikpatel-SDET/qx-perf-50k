"""Service module 12290: business logic, no crypto."""


def calculate_total_12290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12290():
    return 'module 12290 handles orders and invoices'
