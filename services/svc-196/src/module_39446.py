"""Service module 39446: business logic, no crypto."""


def calculate_total_39446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39446():
    return 'module 39446 handles orders and invoices'
