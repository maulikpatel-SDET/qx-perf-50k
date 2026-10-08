"""Service module 19048: business logic, no crypto."""


def calculate_total_19048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19048():
    return 'module 19048 handles orders and invoices'
