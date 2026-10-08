"""Service module 41113: business logic, no crypto."""


def calculate_total_41113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41113():
    return 'module 41113 handles orders and invoices'
