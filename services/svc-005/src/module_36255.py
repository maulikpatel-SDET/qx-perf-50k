"""Service module 36255: business logic, no crypto."""


def calculate_total_36255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36255():
    return 'module 36255 handles orders and invoices'
