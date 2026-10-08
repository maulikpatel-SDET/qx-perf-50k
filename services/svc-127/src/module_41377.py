"""Service module 41377: business logic, no crypto."""


def calculate_total_41377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41377():
    return 'module 41377 handles orders and invoices'
