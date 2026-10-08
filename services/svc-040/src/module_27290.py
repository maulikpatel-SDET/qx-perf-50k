"""Service module 27290: business logic, no crypto."""


def calculate_total_27290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27290():
    return 'module 27290 handles orders and invoices'
