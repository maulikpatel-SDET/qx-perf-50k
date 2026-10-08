"""Service module 41885: business logic, no crypto."""


def calculate_total_41885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41885():
    return 'module 41885 handles orders and invoices'
