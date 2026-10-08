"""Service module 3370: business logic, no crypto."""


def calculate_total_3370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3370():
    return 'module 3370 handles orders and invoices'
