"""Service module 17885: business logic, no crypto."""


def calculate_total_17885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17885():
    return 'module 17885 handles orders and invoices'
