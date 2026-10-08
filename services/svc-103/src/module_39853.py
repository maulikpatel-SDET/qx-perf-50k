"""Service module 39853: business logic, no crypto."""


def calculate_total_39853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39853():
    return 'module 39853 handles orders and invoices'
