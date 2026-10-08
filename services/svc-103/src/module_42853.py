"""Service module 42853: business logic, no crypto."""


def calculate_total_42853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42853():
    return 'module 42853 handles orders and invoices'
