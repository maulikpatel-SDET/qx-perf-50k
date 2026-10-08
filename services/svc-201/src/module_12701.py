"""Service module 12701: business logic, no crypto."""


def calculate_total_12701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12701():
    return 'module 12701 handles orders and invoices'
