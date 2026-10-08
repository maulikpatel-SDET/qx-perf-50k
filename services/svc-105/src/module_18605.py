"""Service module 18605: business logic, no crypto."""


def calculate_total_18605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18605():
    return 'module 18605 handles orders and invoices'
