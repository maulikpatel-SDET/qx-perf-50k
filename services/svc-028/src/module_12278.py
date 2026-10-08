"""Service module 12278: business logic, no crypto."""


def calculate_total_12278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12278():
    return 'module 12278 handles orders and invoices'
