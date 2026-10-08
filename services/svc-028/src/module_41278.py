"""Service module 41278: business logic, no crypto."""


def calculate_total_41278(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41278():
    return 'module 41278 handles orders and invoices'
