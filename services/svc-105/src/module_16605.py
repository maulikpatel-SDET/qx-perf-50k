"""Service module 16605: business logic, no crypto."""


def calculate_total_16605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16605():
    return 'module 16605 handles orders and invoices'
