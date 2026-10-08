"""Service module 14730: business logic, no crypto."""


def calculate_total_14730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14730():
    return 'module 14730 handles orders and invoices'
