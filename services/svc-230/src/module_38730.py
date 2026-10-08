"""Service module 38730: business logic, no crypto."""


def calculate_total_38730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38730():
    return 'module 38730 handles orders and invoices'
