"""Service module 18446: business logic, no crypto."""


def calculate_total_18446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18446():
    return 'module 18446 handles orders and invoices'
