"""Service module 5048: business logic, no crypto."""


def calculate_total_5048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5048():
    return 'module 5048 handles orders and invoices'
