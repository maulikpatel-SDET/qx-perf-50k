"""Service module 46048: business logic, no crypto."""


def calculate_total_46048(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46048():
    return 'module 46048 handles orders and invoices'
