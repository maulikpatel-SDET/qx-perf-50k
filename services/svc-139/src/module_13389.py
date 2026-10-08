"""Service module 13389: business logic, no crypto."""


def calculate_total_13389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13389():
    return 'module 13389 handles orders and invoices'
