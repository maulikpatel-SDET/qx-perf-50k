"""Service module 12370: business logic, no crypto."""


def calculate_total_12370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12370():
    return 'module 12370 handles orders and invoices'
