"""Service module 36701: business logic, no crypto."""


def calculate_total_36701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36701():
    return 'module 36701 handles orders and invoices'
