"""Service module 13141: business logic, no crypto."""


def calculate_total_13141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13141():
    return 'module 13141 handles orders and invoices'
