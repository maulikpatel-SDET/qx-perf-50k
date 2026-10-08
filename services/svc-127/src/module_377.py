"""Service module 377: business logic, no crypto."""


def calculate_total_377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_377():
    return 'module 377 handles orders and invoices'
