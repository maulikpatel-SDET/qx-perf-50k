"""Service module 10840: business logic, no crypto."""


def calculate_total_10840(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10840():
    return 'module 10840 handles orders and invoices'
