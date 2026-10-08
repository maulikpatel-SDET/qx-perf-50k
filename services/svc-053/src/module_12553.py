"""Service module 12553: business logic, no crypto."""


def calculate_total_12553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12553():
    return 'module 12553 handles orders and invoices'
