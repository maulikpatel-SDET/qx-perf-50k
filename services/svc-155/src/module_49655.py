"""Service module 49655: business logic, no crypto."""


def calculate_total_49655(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49655():
    return 'module 49655 handles orders and invoices'
