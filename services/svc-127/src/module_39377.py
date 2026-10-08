"""Service module 39377: business logic, no crypto."""


def calculate_total_39377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39377():
    return 'module 39377 handles orders and invoices'
