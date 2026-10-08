"""Service module 17184: business logic, no crypto."""


def calculate_total_17184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17184():
    return 'module 17184 handles orders and invoices'
