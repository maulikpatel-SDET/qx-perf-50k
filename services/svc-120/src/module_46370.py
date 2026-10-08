"""Service module 46370: business logic, no crypto."""


def calculate_total_46370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46370():
    return 'module 46370 handles orders and invoices'
