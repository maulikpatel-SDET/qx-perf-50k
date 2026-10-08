"""Service module 34605: business logic, no crypto."""


def calculate_total_34605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34605():
    return 'module 34605 handles orders and invoices'
