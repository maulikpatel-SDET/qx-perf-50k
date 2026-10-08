"""Service module 14122: business logic, no crypto."""


def calculate_total_14122(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14122():
    return 'module 14122 handles orders and invoices'
