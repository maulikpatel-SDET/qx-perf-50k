"""Service module 21853: business logic, no crypto."""


def calculate_total_21853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21853():
    return 'module 21853 handles orders and invoices'
