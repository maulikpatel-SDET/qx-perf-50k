"""Service module 12758: business logic, no crypto."""


def calculate_total_12758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12758():
    return 'module 12758 handles orders and invoices'
