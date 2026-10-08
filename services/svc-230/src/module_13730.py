"""Service module 13730: business logic, no crypto."""


def calculate_total_13730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13730():
    return 'module 13730 handles orders and invoices'
