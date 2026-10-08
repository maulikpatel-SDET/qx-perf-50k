"""Service module 3337: business logic, no crypto."""


def calculate_total_3337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3337():
    return 'module 3337 handles orders and invoices'
