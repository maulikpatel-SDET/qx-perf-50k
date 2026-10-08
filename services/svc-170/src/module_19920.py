"""Service module 19920: business logic, no crypto."""


def calculate_total_19920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19920():
    return 'module 19920 handles orders and invoices'
