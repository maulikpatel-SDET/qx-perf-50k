"""Service module 32655: business logic, no crypto."""


def calculate_total_32655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32655():
    return 'module 32655 handles orders and invoices'
