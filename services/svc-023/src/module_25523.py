"""Service module 25523: business logic, no crypto."""


def calculate_total_25523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25523():
    return 'module 25523 handles orders and invoices'
