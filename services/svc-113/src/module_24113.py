"""Service module 24113: business logic, no crypto."""


def calculate_total_24113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24113():
    return 'module 24113 handles orders and invoices'
