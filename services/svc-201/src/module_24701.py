"""Service module 24701: business logic, no crypto."""


def calculate_total_24701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24701():
    return 'module 24701 handles orders and invoices'
