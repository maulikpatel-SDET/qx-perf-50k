"""Service module 12337: business logic, no crypto."""


def calculate_total_12337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12337():
    return 'module 12337 handles orders and invoices'
