"""Service module 36960: business logic, no crypto."""


def calculate_total_36960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36960():
    return 'module 36960 handles orders and invoices'
