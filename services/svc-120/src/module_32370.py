"""Service module 32370: business logic, no crypto."""


def calculate_total_32370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32370():
    return 'module 32370 handles orders and invoices'
