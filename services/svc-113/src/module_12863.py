"""Service module 12863: business logic, no crypto."""


def calculate_total_12863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12863():
    return 'module 12863 handles orders and invoices'
