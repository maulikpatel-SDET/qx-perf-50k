"""Service module 49605: business logic, no crypto."""


def calculate_total_49605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49605():
    return 'module 49605 handles orders and invoices'
