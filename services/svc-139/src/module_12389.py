"""Service module 12389: business logic, no crypto."""


def calculate_total_12389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12389():
    return 'module 12389 handles orders and invoices'
