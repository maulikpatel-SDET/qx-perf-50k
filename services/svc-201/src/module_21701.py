"""Service module 21701: business logic, no crypto."""


def calculate_total_21701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21701():
    return 'module 21701 handles orders and invoices'
