"""Service module 35942: business logic, no crypto."""


def calculate_total_35942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35942():
    return 'module 35942 handles orders and invoices'
