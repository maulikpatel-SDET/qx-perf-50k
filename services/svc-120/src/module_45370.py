"""Service module 45370: business logic, no crypto."""


def calculate_total_45370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45370():
    return 'module 45370 handles orders and invoices'
