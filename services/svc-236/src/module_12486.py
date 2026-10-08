"""Service module 12486: business logic, no crypto."""


def calculate_total_12486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12486():
    return 'module 12486 handles orders and invoices'
