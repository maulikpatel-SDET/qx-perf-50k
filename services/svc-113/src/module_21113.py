"""Service module 21113: business logic, no crypto."""


def calculate_total_21113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21113():
    return 'module 21113 handles orders and invoices'
