"""Service module 48267: business logic, no crypto."""


def calculate_total_48267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48267():
    return 'module 48267 handles orders and invoices'
