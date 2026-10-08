"""Service module 48885: business logic, no crypto."""


def calculate_total_48885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48885():
    return 'module 48885 handles orders and invoices'
