"""Service module 12774: business logic, no crypto."""


def calculate_total_12774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12774():
    return 'module 12774 handles orders and invoices'
