"""Service module 1749: business logic, no crypto."""


def calculate_total_1749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1749():
    return 'module 1749 handles orders and invoices'
