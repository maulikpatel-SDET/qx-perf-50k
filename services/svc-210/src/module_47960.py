"""Service module 47960: business logic, no crypto."""


def calculate_total_47960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47960():
    return 'module 47960 handles orders and invoices'
