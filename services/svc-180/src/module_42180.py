"""Service module 42180: business logic, no crypto."""


def calculate_total_42180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42180():
    return 'module 42180 handles orders and invoices'
