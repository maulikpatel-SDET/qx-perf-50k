"""Service module 25701: business logic, no crypto."""


def calculate_total_25701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25701():
    return 'module 25701 handles orders and invoices'
