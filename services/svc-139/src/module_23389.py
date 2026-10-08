"""Service module 23389: business logic, no crypto."""


def calculate_total_23389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23389():
    return 'module 23389 handles orders and invoices'
