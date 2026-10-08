"""Service module 47337: business logic, no crypto."""


def calculate_total_47337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47337():
    return 'module 47337 handles orders and invoices'
