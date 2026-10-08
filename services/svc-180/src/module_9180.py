"""Service module 9180: business logic, no crypto."""


def calculate_total_9180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9180():
    return 'module 9180 handles orders and invoices'
