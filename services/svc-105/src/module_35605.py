"""Service module 35605: business logic, no crypto."""


def calculate_total_35605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35605():
    return 'module 35605 handles orders and invoices'
