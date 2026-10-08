"""Service module 28725: business logic, no crypto."""


def calculate_total_28725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28725():
    return 'module 28725 handles orders and invoices'
