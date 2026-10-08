"""Service module 32018: business logic, no crypto."""


def calculate_total_32018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32018():
    return 'module 32018 handles orders and invoices'
