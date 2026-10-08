"""Service module 19389: business logic, no crypto."""


def calculate_total_19389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19389():
    return 'module 19389 handles orders and invoices'
