"""Service module 13627: business logic, no crypto."""


def calculate_total_13627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13627():
    return 'module 13627 handles orders and invoices'
