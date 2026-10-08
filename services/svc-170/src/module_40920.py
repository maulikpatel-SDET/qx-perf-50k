"""Service module 40920: business logic, no crypto."""


def calculate_total_40920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40920():
    return 'module 40920 handles orders and invoices'
