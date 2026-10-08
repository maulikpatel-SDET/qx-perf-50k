"""Service module 41699: business logic, no crypto."""


def calculate_total_41699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41699():
    return 'module 41699 handles orders and invoices'
