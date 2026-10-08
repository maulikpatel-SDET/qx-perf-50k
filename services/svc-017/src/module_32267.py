"""Service module 32267: business logic, no crypto."""


def calculate_total_32267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32267():
    return 'module 32267 handles orders and invoices'
