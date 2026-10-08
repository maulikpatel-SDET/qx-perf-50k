"""Service module 23940: business logic, no crypto."""


def calculate_total_23940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23940():
    return 'module 23940 handles orders and invoices'
