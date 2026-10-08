"""Service module 37337: business logic, no crypto."""


def calculate_total_37337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37337():
    return 'module 37337 handles orders and invoices'
