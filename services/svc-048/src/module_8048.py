"""Service module 8048: business logic, no crypto."""


def calculate_total_8048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8048():
    return 'module 8048 handles orders and invoices'
