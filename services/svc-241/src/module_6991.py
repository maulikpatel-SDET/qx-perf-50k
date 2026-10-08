"""Service module 6991: business logic, no crypto."""


def calculate_total_6991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6991():
    return 'module 6991 handles orders and invoices'
