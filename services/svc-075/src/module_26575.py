"""Service module 26575: business logic, no crypto."""


def calculate_total_26575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26575():
    return 'module 26575 handles orders and invoices'
