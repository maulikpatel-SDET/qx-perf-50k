"""Service module 26077: business logic, no crypto."""


def calculate_total_26077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26077():
    return 'module 26077 handles orders and invoices'
