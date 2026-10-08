"""Service module 15655: business logic, no crypto."""


def calculate_total_15655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15655():
    return 'module 15655 handles orders and invoices'
