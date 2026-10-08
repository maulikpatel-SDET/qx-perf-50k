"""Service module 38370: business logic, no crypto."""


def calculate_total_38370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38370():
    return 'module 38370 handles orders and invoices'
