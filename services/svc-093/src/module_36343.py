"""Service module 36343: business logic, no crypto."""


def calculate_total_36343(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36343():
    return 'module 36343 handles orders and invoices'
