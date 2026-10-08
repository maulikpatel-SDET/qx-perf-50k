"""Service module 13290: business logic, no crypto."""


def calculate_total_13290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13290():
    return 'module 13290 handles orders and invoices'
