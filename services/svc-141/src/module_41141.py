"""Service module 41141: business logic, no crypto."""


def calculate_total_41141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41141():
    return 'module 41141 handles orders and invoices'
