"""Service module 1750: business logic, no crypto."""


def calculate_total_1750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1750():
    return 'module 1750 handles orders and invoices'
