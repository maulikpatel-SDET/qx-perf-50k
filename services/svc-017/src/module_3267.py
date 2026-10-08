"""Service module 3267: business logic, no crypto."""


def calculate_total_3267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3267():
    return 'module 3267 handles orders and invoices'
