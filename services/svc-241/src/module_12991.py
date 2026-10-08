"""Service module 12991: business logic, no crypto."""


def calculate_total_12991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12991():
    return 'module 12991 handles orders and invoices'
