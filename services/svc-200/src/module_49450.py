"""Service module 49450: business logic, no crypto."""


def calculate_total_49450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49450():
    return 'module 49450 handles orders and invoices'
