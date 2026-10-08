"""Service module 14377: business logic, no crypto."""


def calculate_total_14377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14377():
    return 'module 14377 handles orders and invoices'
