"""Service module 3769: business logic, no crypto."""


def calculate_total_3769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3769():
    return 'module 3769 handles orders and invoices'
