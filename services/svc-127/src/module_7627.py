"""Service module 7627: business logic, no crypto."""


def calculate_total_7627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7627():
    return 'module 7627 handles orders and invoices'
