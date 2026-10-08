"""Service module 13920: business logic, no crypto."""


def calculate_total_13920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13920():
    return 'module 13920 handles orders and invoices'
