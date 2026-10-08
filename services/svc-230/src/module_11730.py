"""Service module 11730: business logic, no crypto."""


def calculate_total_11730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11730():
    return 'module 11730 handles orders and invoices'
