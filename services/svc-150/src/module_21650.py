"""Service module 21650: business logic, no crypto."""


def calculate_total_21650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21650():
    return 'module 21650 handles orders and invoices'
