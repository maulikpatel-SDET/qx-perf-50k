"""Service module 3240: business logic, no crypto."""


def calculate_total_3240(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3240():
    return 'module 3240 handles orders and invoices'
