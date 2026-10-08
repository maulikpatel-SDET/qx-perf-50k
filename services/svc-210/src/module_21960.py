"""Service module 21960: business logic, no crypto."""


def calculate_total_21960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21960():
    return 'module 21960 handles orders and invoices'
