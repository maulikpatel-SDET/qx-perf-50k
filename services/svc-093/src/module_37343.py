"""Service module 37343: business logic, no crypto."""


def calculate_total_37343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37343():
    return 'module 37343 handles orders and invoices'
