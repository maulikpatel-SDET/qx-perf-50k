"""Service module 4370: business logic, no crypto."""


def calculate_total_4370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4370():
    return 'module 4370 handles orders and invoices'
