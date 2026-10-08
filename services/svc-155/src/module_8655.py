"""Service module 8655: business logic, no crypto."""


def calculate_total_8655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8655():
    return 'module 8655 handles orders and invoices'
