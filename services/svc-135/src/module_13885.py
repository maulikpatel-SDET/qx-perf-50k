"""Service module 13885: business logic, no crypto."""


def calculate_total_13885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13885():
    return 'module 13885 handles orders and invoices'
