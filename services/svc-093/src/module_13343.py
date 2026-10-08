"""Service module 13343: business logic, no crypto."""


def calculate_total_13343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13343():
    return 'module 13343 handles orders and invoices'
