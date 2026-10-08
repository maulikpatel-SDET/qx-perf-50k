"""Service module 3180: business logic, no crypto."""


def calculate_total_3180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3180():
    return 'module 3180 handles orders and invoices'
