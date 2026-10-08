"""Service module 38389: business logic, no crypto."""


def calculate_total_38389(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38389():
    return 'module 38389 handles orders and invoices'
