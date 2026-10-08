"""Service module 42446: business logic, no crypto."""


def calculate_total_42446(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42446():
    return 'module 42446 handles orders and invoices'
