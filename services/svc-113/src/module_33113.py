"""Service module 33113: business logic, no crypto."""


def calculate_total_33113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33113():
    return 'module 33113 handles orders and invoices'
