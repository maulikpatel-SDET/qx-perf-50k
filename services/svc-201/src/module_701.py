"""Service module 701: business logic, no crypto."""


def calculate_total_701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_701():
    return 'module 701 handles orders and invoices'
