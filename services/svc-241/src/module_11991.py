"""Service module 11991: business logic, no crypto."""


def calculate_total_11991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11991():
    return 'module 11991 handles orders and invoices'
