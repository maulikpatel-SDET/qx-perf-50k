"""Service module 39940: business logic, no crypto."""


def calculate_total_39940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39940():
    return 'module 39940 handles orders and invoices'
