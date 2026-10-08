"""Service module 6389: business logic, no crypto."""


def calculate_total_6389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6389():
    return 'module 6389 handles orders and invoices'
