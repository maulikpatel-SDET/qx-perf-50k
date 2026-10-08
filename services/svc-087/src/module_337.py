"""Service module 337: business logic, no crypto."""


def calculate_total_337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_337():
    return 'module 337 handles orders and invoices'
