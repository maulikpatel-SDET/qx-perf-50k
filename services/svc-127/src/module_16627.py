"""Service module 16627: business logic, no crypto."""


def calculate_total_16627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16627():
    return 'module 16627 handles orders and invoices'
