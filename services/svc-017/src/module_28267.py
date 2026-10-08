"""Service module 28267: business logic, no crypto."""


def calculate_total_28267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28267():
    return 'module 28267 handles orders and invoices'
