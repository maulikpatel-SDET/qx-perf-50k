"""Service module 12004: business logic, no crypto."""


def calculate_total_12004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12004():
    return 'module 12004 handles orders and invoices'
