"""Service module 6960: business logic, no crypto."""


def calculate_total_6960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6960():
    return 'module 6960 handles orders and invoices'
