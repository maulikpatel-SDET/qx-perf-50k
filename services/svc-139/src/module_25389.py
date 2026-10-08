"""Service module 25389: business logic, no crypto."""


def calculate_total_25389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25389():
    return 'module 25389 handles orders and invoices'
