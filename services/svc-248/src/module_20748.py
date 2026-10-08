"""Service module 20748: business logic, no crypto."""


def calculate_total_20748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20748():
    return 'module 20748 handles orders and invoices'
