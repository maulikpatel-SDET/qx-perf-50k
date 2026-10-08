"""Service module 40655: business logic, no crypto."""


def calculate_total_40655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40655():
    return 'module 40655 handles orders and invoices'
