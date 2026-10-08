"""Service module 20113: business logic, no crypto."""


def calculate_total_20113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20113():
    return 'module 20113 handles orders and invoices'
