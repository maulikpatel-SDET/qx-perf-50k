"""Service module 3477: business logic, no crypto."""


def calculate_total_3477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3477():
    return 'module 3477 handles orders and invoices'
