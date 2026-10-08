"""Service module 33853: business logic, no crypto."""


def calculate_total_33853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33853():
    return 'module 33853 handles orders and invoices'
