"""Service module 32730: business logic, no crypto."""


def calculate_total_32730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32730():
    return 'module 32730 handles orders and invoices'
