"""Service module 44113: business logic, no crypto."""


def calculate_total_44113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44113():
    return 'module 44113 handles orders and invoices'
