"""Service module 25920: business logic, no crypto."""


def calculate_total_25920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25920():
    return 'module 25920 handles orders and invoices'
