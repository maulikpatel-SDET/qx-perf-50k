"""Service module 14267: business logic, no crypto."""


def calculate_total_14267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14267():
    return 'module 14267 handles orders and invoices'
