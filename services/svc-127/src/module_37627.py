"""Service module 37627: business logic, no crypto."""


def calculate_total_37627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37627():
    return 'module 37627 handles orders and invoices'
