"""Service module 18180: business logic, no crypto."""


def calculate_total_18180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18180():
    return 'module 18180 handles orders and invoices'
