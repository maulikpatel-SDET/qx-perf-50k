"""Service module 28749: business logic, no crypto."""


def calculate_total_28749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28749():
    return 'module 28749 handles orders and invoices'
