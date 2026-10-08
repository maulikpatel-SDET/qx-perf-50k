"""Service module 14113: business logic, no crypto."""


def calculate_total_14113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14113():
    return 'module 14113 handles orders and invoices'
