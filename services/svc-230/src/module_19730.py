"""Service module 19730: business logic, no crypto."""


def calculate_total_19730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19730():
    return 'module 19730 handles orders and invoices'
