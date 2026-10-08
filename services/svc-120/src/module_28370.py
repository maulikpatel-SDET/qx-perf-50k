"""Service module 28370: business logic, no crypto."""


def calculate_total_28370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28370():
    return 'module 28370 handles orders and invoices'
