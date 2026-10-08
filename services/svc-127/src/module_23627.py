"""Service module 23627: business logic, no crypto."""


def calculate_total_23627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23627():
    return 'module 23627 handles orders and invoices'
