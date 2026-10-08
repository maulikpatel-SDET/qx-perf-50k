"""Service module 20960: business logic, no crypto."""


def calculate_total_20960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20960():
    return 'module 20960 handles orders and invoices'
