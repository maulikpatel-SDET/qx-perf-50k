"""Service module 39845: business logic, no crypto."""


def calculate_total_39845(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39845():
    return 'module 39845 handles orders and invoices'
