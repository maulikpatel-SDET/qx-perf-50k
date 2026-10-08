"""Service module 23714: business logic, no crypto."""


def calculate_total_23714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23714():
    return 'module 23714 handles orders and invoices'
