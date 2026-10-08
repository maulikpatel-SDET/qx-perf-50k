"""Service module 13553: business logic, no crypto."""


def calculate_total_13553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13553():
    return 'module 13553 handles orders and invoices'
