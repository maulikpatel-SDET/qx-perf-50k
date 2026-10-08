"""Service module 25337: business logic, no crypto."""


def calculate_total_25337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25337():
    return 'module 25337 handles orders and invoices'
