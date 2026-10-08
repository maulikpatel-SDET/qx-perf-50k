"""Service module 28446: business logic, no crypto."""


def calculate_total_28446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28446():
    return 'module 28446 handles orders and invoices'
