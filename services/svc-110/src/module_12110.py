"""Service module 12110: business logic, no crypto."""


def calculate_total_12110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12110():
    return 'module 12110 handles orders and invoices'
