"""Service module 23113: business logic, no crypto."""


def calculate_total_23113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23113():
    return 'module 23113 handles orders and invoices'
