"""Service module 14141: business logic, no crypto."""


def calculate_total_14141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14141():
    return 'module 14141 handles orders and invoices'
