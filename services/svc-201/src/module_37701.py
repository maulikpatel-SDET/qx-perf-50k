"""Service module 37701: business logic, no crypto."""


def calculate_total_37701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37701():
    return 'module 37701 handles orders and invoices'
