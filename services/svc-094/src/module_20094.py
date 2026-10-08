"""Service module 20094: business logic, no crypto."""


def calculate_total_20094(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20094():
    return 'module 20094 handles orders and invoices'
