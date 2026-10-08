"""Service module 48749: business logic, no crypto."""


def calculate_total_48749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48749():
    return 'module 48749 handles orders and invoices'
