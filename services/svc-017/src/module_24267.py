"""Service module 24267: business logic, no crypto."""


def calculate_total_24267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24267():
    return 'module 24267 handles orders and invoices'
