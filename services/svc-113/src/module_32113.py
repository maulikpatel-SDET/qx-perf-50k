"""Service module 32113: business logic, no crypto."""


def calculate_total_32113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32113():
    return 'module 32113 handles orders and invoices'
