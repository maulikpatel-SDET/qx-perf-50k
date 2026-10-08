"""Service module 36048: business logic, no crypto."""


def calculate_total_36048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36048():
    return 'module 36048 handles orders and invoices'
