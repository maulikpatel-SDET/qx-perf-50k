"""Service module 20389: business logic, no crypto."""


def calculate_total_20389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20389():
    return 'module 20389 handles orders and invoices'
