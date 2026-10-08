"""Service module 34590: business logic, no crypto."""


def calculate_total_34590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34590():
    return 'module 34590 handles orders and invoices'
