"""Service module 37267: business logic, no crypto."""


def calculate_total_37267(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37267():
    return 'module 37267 handles orders and invoices'
