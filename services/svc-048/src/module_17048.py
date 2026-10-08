"""Service module 17048: business logic, no crypto."""


def calculate_total_17048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17048():
    return 'module 17048 handles orders and invoices'
