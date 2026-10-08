"""Service module 42605: business logic, no crypto."""


def calculate_total_42605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42605():
    return 'module 42605 handles orders and invoices'
