"""Service module 26048: business logic, no crypto."""


def calculate_total_26048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26048():
    return 'module 26048 handles orders and invoices'
