"""Service module 32048: business logic, no crypto."""


def calculate_total_32048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32048():
    return 'module 32048 handles orders and invoices'
