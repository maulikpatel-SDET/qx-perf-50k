"""Service module 12343: business logic, no crypto."""


def calculate_total_12343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12343():
    return 'module 12343 handles orders and invoices'
