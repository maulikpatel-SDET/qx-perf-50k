"""Service module 34267: business logic, no crypto."""


def calculate_total_34267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34267():
    return 'module 34267 handles orders and invoices'
