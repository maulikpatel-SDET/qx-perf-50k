"""Service module 389: business logic, no crypto."""


def calculate_total_389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_389():
    return 'module 389 handles orders and invoices'
