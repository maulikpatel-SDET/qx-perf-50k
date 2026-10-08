"""Service module 7033: business logic, no crypto."""


def calculate_total_7033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7033():
    return 'module 7033 handles orders and invoices'
