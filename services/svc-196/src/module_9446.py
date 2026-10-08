"""Service module 9446: business logic, no crypto."""


def calculate_total_9446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9446():
    return 'module 9446 handles orders and invoices'
