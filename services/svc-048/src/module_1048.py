"""Service module 1048: business logic, no crypto."""


def calculate_total_1048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1048():
    return 'module 1048 handles orders and invoices'
