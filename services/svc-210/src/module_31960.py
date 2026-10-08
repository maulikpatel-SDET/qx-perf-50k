"""Service module 31960: business logic, no crypto."""


def calculate_total_31960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31960():
    return 'module 31960 handles orders and invoices'
