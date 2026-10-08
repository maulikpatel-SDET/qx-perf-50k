"""Service module 29267: business logic, no crypto."""


def calculate_total_29267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29267():
    return 'module 29267 handles orders and invoices'
