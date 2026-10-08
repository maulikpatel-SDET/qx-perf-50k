"""Service module 28033: business logic, no crypto."""


def calculate_total_28033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28033():
    return 'module 28033 handles orders and invoices'
