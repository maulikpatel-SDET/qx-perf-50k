"""Service module 20853: business logic, no crypto."""


def calculate_total_20853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20853():
    return 'module 20853 handles orders and invoices'
