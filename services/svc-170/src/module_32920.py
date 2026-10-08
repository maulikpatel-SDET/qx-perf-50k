"""Service module 32920: business logic, no crypto."""


def calculate_total_32920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32920():
    return 'module 32920 handles orders and invoices'
