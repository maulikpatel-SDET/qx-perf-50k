"""Service module 30699: business logic, no crypto."""


def calculate_total_30699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30699():
    return 'module 30699 handles orders and invoices'
