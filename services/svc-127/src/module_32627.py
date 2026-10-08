"""Service module 32627: business logic, no crypto."""


def calculate_total_32627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32627():
    return 'module 32627 handles orders and invoices'
