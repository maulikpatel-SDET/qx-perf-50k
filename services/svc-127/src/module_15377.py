"""Service module 15377: business logic, no crypto."""


def calculate_total_15377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15377():
    return 'module 15377 handles orders and invoices'
