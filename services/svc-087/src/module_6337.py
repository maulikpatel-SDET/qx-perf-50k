"""Service module 6337: business logic, no crypto."""


def calculate_total_6337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6337():
    return 'module 6337 handles orders and invoices'
