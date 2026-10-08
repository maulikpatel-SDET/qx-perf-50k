"""Service module 29389: business logic, no crypto."""


def calculate_total_29389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29389():
    return 'module 29389 handles orders and invoices'
