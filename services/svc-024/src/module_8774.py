"""Service module 8774: business logic, no crypto."""


def calculate_total_8774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8774():
    return 'module 8774 handles orders and invoices'
