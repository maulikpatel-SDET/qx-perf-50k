"""Service module 18389: business logic, no crypto."""


def calculate_total_18389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18389():
    return 'module 18389 handles orders and invoices'
