"""Service module 36920: business logic, no crypto."""


def calculate_total_36920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36920():
    return 'module 36920 handles orders and invoices'
