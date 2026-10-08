"""Service module 7853: business logic, no crypto."""


def calculate_total_7853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7853():
    return 'module 7853 handles orders and invoices'
