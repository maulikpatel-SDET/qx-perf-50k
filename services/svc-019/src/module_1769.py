"""Service module 1769: business logic, no crypto."""


def calculate_total_1769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1769():
    return 'module 1769 handles orders and invoices'
