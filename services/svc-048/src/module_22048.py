"""Service module 22048: business logic, no crypto."""


def calculate_total_22048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22048():
    return 'module 22048 handles orders and invoices'
