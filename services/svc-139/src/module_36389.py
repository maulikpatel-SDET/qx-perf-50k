"""Service module 36389: business logic, no crypto."""


def calculate_total_36389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36389():
    return 'module 36389 handles orders and invoices'
