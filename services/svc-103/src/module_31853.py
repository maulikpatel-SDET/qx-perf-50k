"""Service module 31853: business logic, no crypto."""


def calculate_total_31853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31853():
    return 'module 31853 handles orders and invoices'
