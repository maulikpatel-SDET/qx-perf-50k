"""Service module 31343: business logic, no crypto."""


def calculate_total_31343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31343():
    return 'module 31343 handles orders and invoices'
