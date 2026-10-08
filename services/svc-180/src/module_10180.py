"""Service module 10180: business logic, no crypto."""


def calculate_total_10180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10180():
    return 'module 10180 handles orders and invoices'
