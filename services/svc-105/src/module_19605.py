"""Service module 19605: business logic, no crypto."""


def calculate_total_19605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19605():
    return 'module 19605 handles orders and invoices'
