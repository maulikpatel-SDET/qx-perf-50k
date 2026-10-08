"""Service module 41655: business logic, no crypto."""


def calculate_total_41655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41655():
    return 'module 41655 handles orders and invoices'
