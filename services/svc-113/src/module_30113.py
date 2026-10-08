"""Service module 30113: business logic, no crypto."""


def calculate_total_30113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30113():
    return 'module 30113 handles orders and invoices'
