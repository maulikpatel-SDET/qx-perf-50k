"""Service module 10730: business logic, no crypto."""


def calculate_total_10730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10730():
    return 'module 10730 handles orders and invoices'
