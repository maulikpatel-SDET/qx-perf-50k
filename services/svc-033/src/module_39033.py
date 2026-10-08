"""Service module 39033: business logic, no crypto."""


def calculate_total_39033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39033():
    return 'module 39033 handles orders and invoices'
