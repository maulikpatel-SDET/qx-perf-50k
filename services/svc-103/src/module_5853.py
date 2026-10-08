"""Service module 5853: business logic, no crypto."""


def calculate_total_5853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5853():
    return 'module 5853 handles orders and invoices'
