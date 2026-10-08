"""Service module 36370: business logic, no crypto."""


def calculate_total_36370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36370():
    return 'module 36370 handles orders and invoices'
