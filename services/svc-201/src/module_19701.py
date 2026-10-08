"""Service module 19701: business logic, no crypto."""


def calculate_total_19701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19701():
    return 'module 19701 handles orders and invoices'
