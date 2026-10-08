"""Service module 39477: business logic, no crypto."""


def calculate_total_39477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39477():
    return 'module 39477 handles orders and invoices'
