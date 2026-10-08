"""Service module 36337: business logic, no crypto."""


def calculate_total_36337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36337():
    return 'module 36337 handles orders and invoices'
