"""Service module 30730: business logic, no crypto."""


def calculate_total_30730(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30730():
    return 'module 30730 handles orders and invoices'
