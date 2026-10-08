"""Service module 1960: business logic, no crypto."""


def calculate_total_1960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1960():
    return 'module 1960 handles orders and invoices'
