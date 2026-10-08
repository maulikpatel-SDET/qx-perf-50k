"""Service module 1758: business logic, no crypto."""


def calculate_total_1758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1758():
    return 'module 1758 handles orders and invoices'
