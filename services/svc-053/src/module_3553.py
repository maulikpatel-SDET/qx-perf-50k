"""Service module 3553: business logic, no crypto."""


def calculate_total_3553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3553():
    return 'module 3553 handles orders and invoices'
