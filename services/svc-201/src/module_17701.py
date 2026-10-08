"""Service module 17701: business logic, no crypto."""


def calculate_total_17701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17701():
    return 'module 17701 handles orders and invoices'
