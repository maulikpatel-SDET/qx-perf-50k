"""Service module 26113: business logic, no crypto."""


def calculate_total_26113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26113():
    return 'module 26113 handles orders and invoices'
