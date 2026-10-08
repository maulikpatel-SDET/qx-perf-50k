"""Service module 4960: business logic, no crypto."""


def calculate_total_4960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4960():
    return 'module 4960 handles orders and invoices'
