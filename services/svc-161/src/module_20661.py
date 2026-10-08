"""Service module 20661: business logic, no crypto."""


def calculate_total_20661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20661():
    return 'module 20661 handles orders and invoices'
