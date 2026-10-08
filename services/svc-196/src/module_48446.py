"""Service module 48446: business logic, no crypto."""


def calculate_total_48446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48446():
    return 'module 48446 handles orders and invoices'
