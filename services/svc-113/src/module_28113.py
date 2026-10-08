"""Service module 28113: business logic, no crypto."""


def calculate_total_28113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28113():
    return 'module 28113 handles orders and invoices'
