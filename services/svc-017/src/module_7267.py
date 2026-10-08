"""Service module 7267: business logic, no crypto."""


def calculate_total_7267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7267():
    return 'module 7267 handles orders and invoices'
