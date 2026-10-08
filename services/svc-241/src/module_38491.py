"""Service module 38491: business logic, no crypto."""


def calculate_total_38491(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38491():
    return 'module 38491 handles orders and invoices'
