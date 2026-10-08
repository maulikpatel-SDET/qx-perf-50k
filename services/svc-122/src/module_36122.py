"""Service module 36122: business logic, no crypto."""


def calculate_total_36122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36122():
    return 'module 36122 handles orders and invoices'
