"""Service module 20920: business logic, no crypto."""


def calculate_total_20920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20920():
    return 'module 20920 handles orders and invoices'
