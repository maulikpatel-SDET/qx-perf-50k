"""Service module 44920: business logic, no crypto."""


def calculate_total_44920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44920():
    return 'module 44920 handles orders and invoices'
