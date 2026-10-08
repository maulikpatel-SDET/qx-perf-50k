"""Service module 35255: business logic, no crypto."""


def calculate_total_35255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35255():
    return 'module 35255 handles orders and invoices'
