"""Service module 5267: business logic, no crypto."""


def calculate_total_5267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5267():
    return 'module 5267 handles orders and invoices'
