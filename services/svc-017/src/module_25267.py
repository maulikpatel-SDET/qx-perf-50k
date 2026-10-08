"""Service module 25267: business logic, no crypto."""


def calculate_total_25267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25267():
    return 'module 25267 handles orders and invoices'
