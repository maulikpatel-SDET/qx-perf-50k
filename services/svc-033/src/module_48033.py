"""Service module 48033: business logic, no crypto."""


def calculate_total_48033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48033():
    return 'module 48033 handles orders and invoices'
