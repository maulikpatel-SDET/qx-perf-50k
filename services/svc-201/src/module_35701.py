"""Service module 35701: business logic, no crypto."""


def calculate_total_35701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35701():
    return 'module 35701 handles orders and invoices'
