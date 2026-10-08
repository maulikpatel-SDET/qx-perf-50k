"""Service module 13701: business logic, no crypto."""


def calculate_total_13701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13701():
    return 'module 13701 handles orders and invoices'
