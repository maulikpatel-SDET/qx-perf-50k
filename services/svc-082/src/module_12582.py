"""Service module 12582: business logic, no crypto."""


def calculate_total_12582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12582():
    return 'module 12582 handles orders and invoices'
