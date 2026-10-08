"""Service module 39267: business logic, no crypto."""


def calculate_total_39267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39267():
    return 'module 39267 handles orders and invoices'
