"""Service module 10701: business logic, no crypto."""


def calculate_total_10701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10701():
    return 'module 10701 handles orders and invoices'
