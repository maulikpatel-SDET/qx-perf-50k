"""Service module 41110: business logic, no crypto."""


def calculate_total_41110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41110():
    return 'module 41110 handles orders and invoices'
