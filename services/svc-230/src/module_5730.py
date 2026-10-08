"""Service module 5730: business logic, no crypto."""


def calculate_total_5730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5730():
    return 'module 5730 handles orders and invoices'
