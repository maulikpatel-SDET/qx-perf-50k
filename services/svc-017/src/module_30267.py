"""Service module 30267: business logic, no crypto."""


def calculate_total_30267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30267():
    return 'module 30267 handles orders and invoices'
