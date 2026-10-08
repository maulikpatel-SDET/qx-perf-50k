"""Service module 7605: business logic, no crypto."""


def calculate_total_7605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7605():
    return 'module 7605 handles orders and invoices'
