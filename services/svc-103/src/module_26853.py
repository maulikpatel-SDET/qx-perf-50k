"""Service module 26853: business logic, no crypto."""


def calculate_total_26853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26853():
    return 'module 26853 handles orders and invoices'
