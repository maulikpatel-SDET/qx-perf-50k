"""Service module 23655: business logic, no crypto."""


def calculate_total_23655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23655():
    return 'module 23655 handles orders and invoices'
