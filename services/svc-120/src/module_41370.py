"""Service module 41370: business logic, no crypto."""


def calculate_total_41370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41370():
    return 'module 41370 handles orders and invoices'
