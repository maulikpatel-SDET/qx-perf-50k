"""Service module 5590: business logic, no crypto."""


def calculate_total_5590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5590():
    return 'module 5590 handles orders and invoices'
