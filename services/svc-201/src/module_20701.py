"""Service module 20701: business logic, no crypto."""


def calculate_total_20701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20701():
    return 'module 20701 handles orders and invoices'
