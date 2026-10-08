"""Service module 48110: business logic, no crypto."""


def calculate_total_48110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48110():
    return 'module 48110 handles orders and invoices'
