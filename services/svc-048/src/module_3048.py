"""Service module 3048: business logic, no crypto."""


def calculate_total_3048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3048():
    return 'module 3048 handles orders and invoices'
