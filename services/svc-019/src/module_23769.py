"""Service module 23769: business logic, no crypto."""


def calculate_total_23769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23769():
    return 'module 23769 handles orders and invoices'
