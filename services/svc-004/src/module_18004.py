"""Service module 18004: business logic, no crypto."""


def calculate_total_18004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18004():
    return 'module 18004 handles orders and invoices'
