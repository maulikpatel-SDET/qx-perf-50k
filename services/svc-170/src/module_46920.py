"""Service module 46920: business logic, no crypto."""


def calculate_total_46920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46920():
    return 'module 46920 handles orders and invoices'
