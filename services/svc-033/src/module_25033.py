"""Service module 25033: business logic, no crypto."""


def calculate_total_25033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25033():
    return 'module 25033 handles orders and invoices'
