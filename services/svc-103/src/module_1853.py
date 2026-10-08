"""Service module 1853: business logic, no crypto."""


def calculate_total_1853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1853():
    return 'module 1853 handles orders and invoices'
