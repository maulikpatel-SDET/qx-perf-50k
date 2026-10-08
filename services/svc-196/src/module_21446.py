"""Service module 21446: business logic, no crypto."""


def calculate_total_21446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21446():
    return 'module 21446 handles orders and invoices'
