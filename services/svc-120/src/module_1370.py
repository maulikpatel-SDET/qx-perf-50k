"""Service module 1370: business logic, no crypto."""


def calculate_total_1370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1370():
    return 'module 1370 handles orders and invoices'
