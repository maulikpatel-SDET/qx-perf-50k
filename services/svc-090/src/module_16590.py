"""Service module 16590: business logic, no crypto."""


def calculate_total_16590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16590():
    return 'module 16590 handles orders and invoices'
