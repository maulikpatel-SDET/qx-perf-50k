"""Service module 38267: business logic, no crypto."""


def calculate_total_38267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38267():
    return 'module 38267 handles orders and invoices'
