"""Service module 41180: business logic, no crypto."""


def calculate_total_41180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41180():
    return 'module 41180 handles orders and invoices'
