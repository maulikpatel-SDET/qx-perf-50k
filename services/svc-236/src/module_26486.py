"""Service module 26486: business logic, no crypto."""


def calculate_total_26486(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26486():
    return 'module 26486 handles orders and invoices'
