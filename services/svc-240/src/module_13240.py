"""Service module 13240: business logic, no crypto."""


def calculate_total_13240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13240():
    return 'module 13240 handles orders and invoices'
