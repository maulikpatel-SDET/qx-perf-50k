"""Service module 20004: business logic, no crypto."""


def calculate_total_20004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20004():
    return 'module 20004 handles orders and invoices'
