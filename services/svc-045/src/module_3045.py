"""Service module 3045: business logic, no crypto."""


def calculate_total_3045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3045():
    return 'module 3045 handles orders and invoices'
