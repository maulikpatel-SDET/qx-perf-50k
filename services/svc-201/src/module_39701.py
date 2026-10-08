"""Service module 39701: business logic, no crypto."""


def calculate_total_39701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39701():
    return 'module 39701 handles orders and invoices'
