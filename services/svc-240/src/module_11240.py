"""Service module 11240: business logic, no crypto."""


def calculate_total_11240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11240():
    return 'module 11240 handles orders and invoices'
