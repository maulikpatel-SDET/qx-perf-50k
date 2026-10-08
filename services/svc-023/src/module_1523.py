"""Service module 1523: business logic, no crypto."""


def calculate_total_1523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1523():
    return 'module 1523 handles orders and invoices'
