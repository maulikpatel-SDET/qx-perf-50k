"""Service module 1337: business logic, no crypto."""


def calculate_total_1337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1337():
    return 'module 1337 handles orders and invoices'
