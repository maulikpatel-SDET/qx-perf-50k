"""Service module 13650: business logic, no crypto."""


def calculate_total_13650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13650():
    return 'module 13650 handles orders and invoices'
