"""Service module 26377: business logic, no crypto."""


def calculate_total_26377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26377():
    return 'module 26377 handles orders and invoices'
