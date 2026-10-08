"""Service module 3885: business logic, no crypto."""


def calculate_total_3885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3885():
    return 'module 3885 handles orders and invoices'
