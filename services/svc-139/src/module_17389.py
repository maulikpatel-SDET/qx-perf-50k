"""Service module 17389: business logic, no crypto."""


def calculate_total_17389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17389():
    return 'module 17389 handles orders and invoices'
