"""Service module 39113: business logic, no crypto."""


def calculate_total_39113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39113():
    return 'module 39113 handles orders and invoices'
