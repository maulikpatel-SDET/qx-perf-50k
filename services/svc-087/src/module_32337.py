"""Service module 32337: business logic, no crypto."""


def calculate_total_32337(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32337():
    return 'module 32337 handles orders and invoices'
