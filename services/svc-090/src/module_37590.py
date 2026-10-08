"""Service module 37590: business logic, no crypto."""


def calculate_total_37590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37590():
    return 'module 37590 handles orders and invoices'
