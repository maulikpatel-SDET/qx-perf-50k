"""Service module 14343: business logic, no crypto."""


def calculate_total_14343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14343():
    return 'module 14343 handles orders and invoices'
