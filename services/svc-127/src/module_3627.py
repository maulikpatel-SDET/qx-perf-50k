"""Service module 3627: business logic, no crypto."""


def calculate_total_3627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3627():
    return 'module 3627 handles orders and invoices'
