"""Service module 28655: business logic, no crypto."""


def calculate_total_28655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28655():
    return 'module 28655 handles orders and invoices'
