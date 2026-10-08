"""Service module 40048: business logic, no crypto."""


def calculate_total_40048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40048():
    return 'module 40048 handles orders and invoices'
