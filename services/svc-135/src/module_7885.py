"""Service module 7885: business logic, no crypto."""


def calculate_total_7885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7885():
    return 'module 7885 handles orders and invoices'
