"""Service module 41553: business logic, no crypto."""


def calculate_total_41553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41553():
    return 'module 41553 handles orders and invoices'
