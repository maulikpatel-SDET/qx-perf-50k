"""Service module 30605: business logic, no crypto."""


def calculate_total_30605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30605():
    return 'module 30605 handles orders and invoices'
