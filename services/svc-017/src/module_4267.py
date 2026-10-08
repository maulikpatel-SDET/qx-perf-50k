"""Service module 4267: business logic, no crypto."""


def calculate_total_4267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4267():
    return 'module 4267 handles orders and invoices'
