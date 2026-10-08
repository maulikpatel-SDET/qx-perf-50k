"""Service module 13450: business logic, no crypto."""


def calculate_total_13450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13450():
    return 'module 13450 handles orders and invoices'
