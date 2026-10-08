"""Service module 7389: business logic, no crypto."""


def calculate_total_7389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7389():
    return 'module 7389 handles orders and invoices'
