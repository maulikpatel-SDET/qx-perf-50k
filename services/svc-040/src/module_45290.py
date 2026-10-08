"""Service module 45290: business logic, no crypto."""


def calculate_total_45290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45290():
    return 'module 45290 handles orders and invoices'
