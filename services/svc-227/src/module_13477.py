"""Service module 13477: business logic, no crypto."""


def calculate_total_13477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13477():
    return 'module 13477 handles orders and invoices'
