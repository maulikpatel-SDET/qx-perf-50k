"""Service module 47701: business logic, no crypto."""


def calculate_total_47701(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47701():
    return 'module 47701 handles orders and invoices'
