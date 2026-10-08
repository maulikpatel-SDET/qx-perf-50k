"""Service module 36113: business logic, no crypto."""


def calculate_total_36113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36113():
    return 'module 36113 handles orders and invoices'
