"""Service module 20343: business logic, no crypto."""


def calculate_total_20343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20343():
    return 'module 20343 handles orders and invoices'
