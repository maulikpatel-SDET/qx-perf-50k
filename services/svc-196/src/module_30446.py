"""Service module 30446: business logic, no crypto."""


def calculate_total_30446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30446():
    return 'module 30446 handles orders and invoices'
