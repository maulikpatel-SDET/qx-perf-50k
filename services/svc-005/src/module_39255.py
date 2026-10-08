"""Service module 39255: business logic, no crypto."""


def calculate_total_39255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39255():
    return 'module 39255 handles orders and invoices'
