"""Service module 13113: business logic, no crypto."""


def calculate_total_13113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13113():
    return 'module 13113 handles orders and invoices'
