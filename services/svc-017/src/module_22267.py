"""Service module 22267: business logic, no crypto."""


def calculate_total_22267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22267():
    return 'module 22267 handles orders and invoices'
