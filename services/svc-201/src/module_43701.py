"""Service module 43701: business logic, no crypto."""


def calculate_total_43701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43701():
    return 'module 43701 handles orders and invoices'
