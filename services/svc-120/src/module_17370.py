"""Service module 17370: business logic, no crypto."""


def calculate_total_17370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17370():
    return 'module 17370 handles orders and invoices'
