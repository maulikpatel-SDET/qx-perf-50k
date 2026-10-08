"""Service module 32701: business logic, no crypto."""


def calculate_total_32701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32701():
    return 'module 32701 handles orders and invoices'
