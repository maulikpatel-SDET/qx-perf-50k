"""Service module 47655: business logic, no crypto."""


def calculate_total_47655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47655():
    return 'module 47655 handles orders and invoices'
