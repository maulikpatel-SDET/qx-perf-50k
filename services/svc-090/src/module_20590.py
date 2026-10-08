"""Service module 20590: business logic, no crypto."""


def calculate_total_20590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20590():
    return 'module 20590 handles orders and invoices'
