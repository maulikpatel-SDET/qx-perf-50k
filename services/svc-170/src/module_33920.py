"""Service module 33920: business logic, no crypto."""


def calculate_total_33920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33920():
    return 'module 33920 handles orders and invoices'
