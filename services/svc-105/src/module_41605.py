"""Service module 41605: business logic, no crypto."""


def calculate_total_41605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41605():
    return 'module 41605 handles orders and invoices'
