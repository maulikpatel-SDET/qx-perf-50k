"""Service module 20450: business logic, no crypto."""


def calculate_total_20450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20450():
    return 'module 20450 handles orders and invoices'
