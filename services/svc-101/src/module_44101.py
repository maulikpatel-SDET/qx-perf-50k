"""Service module 44101: business logic, no crypto."""


def calculate_total_44101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44101():
    return 'module 44101 handles orders and invoices'
