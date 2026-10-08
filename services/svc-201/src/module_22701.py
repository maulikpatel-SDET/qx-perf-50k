"""Service module 22701: business logic, no crypto."""


def calculate_total_22701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22701():
    return 'module 22701 handles orders and invoices'
