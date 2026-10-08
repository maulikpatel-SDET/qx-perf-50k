"""Service module 42920: business logic, no crypto."""


def calculate_total_42920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42920():
    return 'module 42920 handles orders and invoices'
