"""Service module 35370: business logic, no crypto."""


def calculate_total_35370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35370():
    return 'module 35370 handles orders and invoices'
