"""Service module 1377: business logic, no crypto."""


def calculate_total_1377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1377():
    return 'module 1377 handles orders and invoices'
