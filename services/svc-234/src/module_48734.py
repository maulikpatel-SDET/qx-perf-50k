"""Service module 48734: business logic, no crypto."""


def calculate_total_48734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48734():
    return 'module 48734 handles orders and invoices'
