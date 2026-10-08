"""Service module 37477: business logic, no crypto."""


def calculate_total_37477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37477():
    return 'module 37477 handles orders and invoices'
