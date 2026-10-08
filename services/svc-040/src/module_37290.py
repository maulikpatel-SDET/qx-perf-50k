"""Service module 37290: business logic, no crypto."""


def calculate_total_37290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37290():
    return 'module 37290 handles orders and invoices'
