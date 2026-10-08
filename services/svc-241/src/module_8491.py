"""Service module 8491: business logic, no crypto."""


def calculate_total_8491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8491():
    return 'module 8491 handles orders and invoices'
